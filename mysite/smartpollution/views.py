from django.shortcuts import render, get_object_or_404, redirect

from django.http import HttpResponse, Http404
from django.template import loader
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.views import generic
from smartpollution.forms import *

from .models import Device, Metric, Template, Threshold


class IndexView(generic.ListView):
    template_name = 'smartpollution/index.html'
    context_object_name = 'device_name_list'

    def get_queryset(self):
        """Return the last five published questions."""
        return Device.objects.order_by('-device_name')[:5]


def DetailView(request, pk):
    arguments={}
    arguments['pk']=pk
    arguments['device']=Device.objects.get(id=pk)
    arguments['templates']=Template.objects.filter(device=Device.objects.get(id=pk))
    return render(request, 'smartpollution/detail.html', arguments)

def DetailViewTemplate(request, pk):
    arguments={}
    arguments['pk']=pk
    arguments['device']=Template.objects.get(id=pk).device

    arguments['template']=Template.objects.get(id=pk)
    arguments['thresholds']=Threshold.objects.filter(template=Template.objects.filter())
    return render(request, 'smartpollution/detail_template.html', arguments)

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
        device=Device.objects.get(id=pk)
        print()
        template = Template(device=device)
        for key, value in request.POST.items() :
            print("Round")
            print("key is:" + key + "   value is:" + value)
            if len(value)>0:
                if "lower:" in key or "upper:" in key:
                    print("Adding key:"+str(key))
                    metric=Metric.objects.get(id=key.strip("lower:").strip("upper:"))
                    if Threshold.objects.filter(template=template, metric=metric).exists():
                        threshold=Threshold.objects.get(template=template, metric=metric)
                        if "lower:" in key:
                            threshold.lower_trigger=value
                        if "upper:" in key:
                            threshold.upper_trigger=value
                        threshold.save()
                    else:
                        threshold=Threshold(template=template, metric=metric)
                        if "lower:" in key:
                            threshold.lower_trigger=value
                        if "upper:" in key:
                            threshold.upper_trigger=value
                        threshold.save()
                if "template_name" in key:
                    print("Adding name")
                    template.template_name=value
                    template.save()
                    print("Name tempalet added:"+value)
            print("For one roudn")
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