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


def index_view(request):
    """
    return the mainpage
    :param request: 
    :return: 
    """
    try:
        arguments = {}
        arguments['device_list'] = Device.objects.all()
        return render(request, 'smartpollution/index.html', arguments)
    except:
        pass


def index_template_view(request):
    """
    returns the template index
    :param request: 
    :return: 
    """
    try:
        arguments = {}
        arguments['template_list'] = Template.objects.all()
        return render(request, 'smartpollution/index_template.html', arguments)
    except:
        pass


def device_search_view(request):
    """
    return the results of the  device search
    :param request: the search string defined by the user
    :return: the found results
    """
    try:
        arguments = {}
        if request.POST:
            for key, value in request.POST.items():
                if "deviceSearch" in key:
                    arguments['device_list'] = Device.objects.all()
                    arguments['device_found'] = Device.objects.filter(Q(device_name__icontains=value)| Q(manufacturing_company__icontains=value))
        return render(request, 'smartpollution/index.html', arguments)
    except:
        pass


def about_view(request):
    """
    return the about view, sepcifiying contact data and infos about the project
    :param request: 
    :return: 
    """
    try:
        return render(request, 'smartpollution/about.html')
    except:
        pass


def detail_view(request, pk):
    """
    returns the details of a device
    :param request:
    :param pk: the pk of the device to display
    :return: the details of the device
    """
    try:
        arguments = {}
        arguments['pk'] = pk
        arguments['device'] = Device.objects.get(id=pk)
        arguments['templates'] = Template.objects.filter(device=Device.objects.get(id=pk))
        return render(request, 'smartpollution/detail.html', arguments)
    except:
        pass


def detail_template_view(request, pk):
    """
    returns the detail view of a tempalte
    :param request: 
    :param pk: the pk of a template to display
    :return: the details of a template
    """
    try:
        arguments = {}
        arguments['pk'] = pk
        arguments['device'] = Template.objects.get(id=pk).device
        arguments['template'] = Template.objects.get(id=pk)
        arguments['thresholds'] = Threshold.objects.filter(template=Template.objects.get(id=pk))
        return render(request, 'smartpollution/detail_template.html', arguments)
    except:
        pass


def register_device_view(request):
    """
    return the input form for a device registration
    :param request: 
    :return: 
    """
    try:
        return render(request, 'smartpollution/register_device.html')
    except:
        pass


def register_metric_view(request):
    """
    return the input form for a metric registration
    :param request: 
    :return: 
    """
    try:
        return render(request, 'smartpollution/register_metric.html')
    except:
        pass
