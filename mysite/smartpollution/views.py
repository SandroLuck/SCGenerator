from django.shortcuts import render, get_object_or_404, redirect

from django.http import HttpResponse, Http404
from django.template import loader
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.views import generic
from smartpollution.forms import *

from .models import Choice, Question, Device, Metric, Template, Threshold


class IndexView(generic.ListView):
    template_name = 'smartpollution/index.html'
    context_object_name = 'device_name_list'

    def get_queryset(self):
        """Return the last five published questions."""
        return Device.objects.order_by('-device_name')[:5]


class DetailView(generic.DetailView):
    model = Device
    template_name = 'smartpollution/detail.html'

class ResultsView(generic.DetailView):
    model = Question
    template_name = 'smartpollution/results.html'


#def AddMetricToDeviceView (request, pk):
#    context={ 'pk' : pk, 'metrics':Metric.objects.all()}
#    print("Add metric to device")
#    return render(request,'smartpollution/add_metric_to_device.html', context)

def AddMetricToDevice(request, pk):
    arguments={}
    arguments['pk']=pk
    arguments['metrics']=Metric.objects.all()
    return render(request, 'smartpollution/add_metric_to_device.html', arguments)

def AddTemplateToDevice(request, pk):
    arguments={}
    arguments['pk']=pk
    arguments['metrics_of_device']=Device.objects.get(id=pk).metrics.all()
    return render(request, 'smartpollution/add_template_to_device.html', arguments)


class RegisterDeviceView(generic.FormView):
    template_name = 'smartpollution/register_device.html'
    form_class = RegisterDeviceForm
    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        return super(RegisterDeviceView, self).form_valid(form)

class RegisterMetricView(generic.FormView):
    template_name = 'smartpollution/register_metric.html'
    form_class = RegisterMetricForm
    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        return super(RegisterDeviceView, self).form_valid(form)

def addDevice(request):
        if request.POST:
            form= RegisterDeviceForm(request.POST)
            if form.is_valid():
                device_n=form.cleaned_data['device_name']
                manufacturing_c=form.cleaned_data['manufacturing_company']
                device=Device(manufacturing_company=manufacturing_c, device_name=device_n)
                device.save()
        return redirect('smartpollution:index')

def saveMetricToDevice(request, pk):
    if request.POST:
        for key, value in request.POST.items():
            if key.isdigit():
                met=Metric.objects.get(id=key)
                print(met)
                dev=Device.objects.get(id=pk)
                print(dev)
                dev.metrics.add(met)
                print(dev.metrics.all())
    return redirect('smartpollution:index')

def saveTemplateToDevice(request, pk):
    if request.POST:
        template = Template(device_id=pk)
        template.save()
        for key, value in request.POST.items() :
            if len(value)>0:
                print("key is:"+key+"   value is:"+value)
                if "lower" or "upper "in key:
                    if Threshold.objects.filter(template_id=pk, metric_id=key.strip("lower:").strip("upper:")).exists():
                        threshold=Threshold.objects.get(template_id=template.id, metric_id=key.strip("lower:").strip("upper:"))
                        if "lower:" in key:
                            threshold.lower_trigger=value
                        if "upper:" in key:
                            threshold.upper_trigger=value
                        threshold.save()
                    else:
                        threshold=Threshold(template_id=template.id, metric_id=key.strip("lower:").strip("upper:"))
                        if "lower:" in key:
                            threshold.lower_trigger=value
                        if "upper:" in key:
                            threshold.upper_trigger=value
                        threshold.save()
                if "template_name" in key:
                    template.template_name=value
                    template.save()
                    print("name")

    return redirect('smartpollution:index')

def addMetric(request):
    if request.POST:
        form = RegisterMetricForm(request.POST)
        if form.is_valid():
            physical_p = form.cleaned_data['physical_property']
            unit_of_m = form.cleaned_data['unit_of_measurement']
            metric = Metric(physical_property=physical_p, unit_of_measurement=unit_of_m)
            metric.save()
    return redirect('smartpollution:index')


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'smartpollution/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('smartpollution:results', args=(question.id,)))