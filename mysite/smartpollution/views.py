from django.shortcuts import render, get_object_or_404, redirect

from django.http import HttpResponse, Http404
from django.template import loader
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.views import generic
from smartpollution.forms import *
from django.db.models import Q


from .models import Device, Metric, Template, Threshold


def IndexView(request):
    arguments = {}
    arguments['device_list'] = Device.objects.all()
    return render(request, 'smartpollution/index.html', arguments)


def IndexTemplateView(request):
    arguments = {}
    arguments['template_list'] = Template.objects.all()
    return render(request, 'smartpollution/index_template.html', arguments)


def DeviceSearchView(request):
    arguments = {}
    if request.POST:
        for key, value in request.POST.items():
            if "deviceSearch" in key:
                arguments['device_list'] = Device.objects.all()
                arguments['device_found'] = Device.objects.filter(Q(device_name__icontains=value)| Q(manufacturing_company__icontains=value))
    return render(request, 'smartpollution/index.html', arguments)


def AboutView(request):
    return render(request, 'smartpollution/about.html')


def DetailView(request, pk):
    arguments = {}
    arguments['pk'] = pk
    arguments['device'] = Device.objects.get(id=pk)
    arguments['templates'] = Template.objects.filter(device=Device.objects.get(id=pk))
    return render(request, 'smartpollution/detail.html', arguments)


def DetailTemplateView(request, pk):
    arguments = {}
    arguments['pk'] = pk
    arguments['device'] = Template.objects.get(id=pk).device
    arguments['template'] = Template.objects.get(id=pk)
    arguments['thresholds'] = Threshold.objects.filter(template=Template.objects.get(id=pk))
    return render(request, 'smartpollution/detail_template.html', arguments)


def AddMetricToDevice(request, pk):
    arguments = {}
    arguments['pk'] = pk
    arguments['metrics'] = Metric.objects.all()
    return render(request, 'smartpollution/add_metric_to_device.html', arguments)


def AddTemplateToDevice(request, pk):
    arguments = {}
    arguments['pk'] = pk
    arguments['metrics_of_device'] = Device.objects.get(id=pk).metrics.all()
    return render(request, 'smartpollution/add_template_to_device.html', arguments)


def RegisterDeviceView(request):
    return render(request, 'smartpollution/register_device.html')


def RegisterMetricView(request):
    return render(request, 'smartpollution/register_metric.html')


def addDevice(request):
    if request.POST:
        form = RegisterDeviceForm(request.POST)
        if form.is_valid():
            device_n = form.cleaned_data['device_name']
            manufacturing_c = form.cleaned_data['manufacturing_company']
            device = Device(manufacturing_company=manufacturing_c, device_name=device_n)
            device.save()
    return redirect('smartpollution:index')


def saveMetricToDevice(request, pk):
    if request.POST:
        for key, value in request.POST.items():
            if key.isdigit():
                met = Metric.objects.get(id=key)
                dev = Device.objects.get(id=pk)
                dev.metrics.add(met)
    return redirect('smartpollution:index')


def saveTemplateToDevice(request, pk):
    if request.POST:
        device = Device.objects.get(id=pk)
        template = Template(device=device)
        for key, value in request.POST.items():
            if len(value) > 0:
                if "lower:" in key or "upper:" in key:
                    metric = Metric.objects.get(id=key.strip("lower:").strip("upper:"))
                    if Threshold.objects.filter(template=template, metric=metric).exists():
                        threshold = Threshold.objects.get(template=template, metric=metric)
                        if "lower:" in key:
                            threshold.lower_trigger = value
                        if "upper:" in key:
                            threshold.upper_trigger = value
                        threshold.save()
                    else:
                        threshold = Threshold(template=template, metric=metric)
                        if "lower:" in key:
                            threshold.lower_trigger = value
                        if "upper:" in key:
                            threshold.upper_trigger = value
                        threshold.save()
                if "template_name" in key:
                    template.template_name = value
                    template.save()
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
