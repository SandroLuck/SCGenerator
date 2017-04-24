from django.shortcuts import render, get_object_or_404, redirect

from django.http import HttpResponse, Http404
from django.template import loader
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.views import generic
from smartpollution.forms import RegisterDeviceForm, RegisterMetricForm

from .models import Choice, Question, Device, Metric


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


def AddMetricToDeviceView (request, pk):
    context={ pk : 'pk', Metric.objects.all() : 'objs'}
    return render(request, 'smartpollution/add_metric_to_device.html', context )


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