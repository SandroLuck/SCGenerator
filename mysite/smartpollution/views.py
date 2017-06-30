from django.shortcuts import render, get_object_or_404, redirect

from django.http import HttpResponse, Http404
from django.template import loader
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.views import generic
from smartpollution.forms import *
from django.db.models import Q

from smartpollution.read_eth_chain import get_contract_info
from .generate_smartcontract import create_new_smart_contract

from .models import Device, Metric, Template, Threshold, Contract

import os


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
        return return_problem_page(request)



def index_template_view(request):
    """
    returns the template index
    :param request: 
    :return: 
    """
    try:
        arguments = {}
        arguments['template_list'] = Template.objects.all()
        return render(request, 'smartpollution/indextemplate.html', arguments)
    except:
        return return_problem_page(request)



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
        return return_problem_page(request)



def about_view(request):
    """
    return the about view, sepcifiying contact data and infos about the project
    :param request: 
    :return: 
    """
    try:
        return render(request, 'smartpollution/about.html')
    except:
        return return_problem_page(request)



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
        return return_problem_page(request)



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
        arguments['cost_thres'] = Template.objects.get(id=pk).gas_estimate_thres
        arguments['cost_no_thres'] = Template.objects.get(id=pk).gas_estimate_no_thres
        return render(request, 'smartpollution/detailtemplate.html', arguments)
    except:
        return return_problem_page(request)

def detail_contract_view(request, pk):
    """
    returns the detail view of a contract
    :param request: 
    :param pk: the pk of a contract to display
    :return: the details of a contract
    """
    try:
        print("Start cotnract detail")
        arguments = {}
        contract=Contract.objects.get(id=pk)
        arguments['contract'] = contract
        arguments['info']=get_contract_info(abi=contract.contract_abi, address=contract.contract_address)

        return render(request, 'smartpollution/detailcontract.html', arguments)
    except Exception as e:
        print(str(e))
        return return_problem_page(request)


def register_device_view(request):
    """
    return the input form for a device registration
    :param request: 
    :return: 
    """
    try:
        return render(request, 'smartpollution/registerdevice.html')
    except:
        return return_problem_page(request)


def register_metric_view(request):
    """
    return the input form for a metric registration
    :param request: 
    :return: 
    """
    try:
        return render(request, 'smartpollution/registermetric.html')
    except:
        return return_problem_page(request)

def register_contract_view(request):
    """
    return the input form for a metric registration
    :param request: 
    :return: 
    """
    try:
        return render(request, 'smartpollution/registercontract.html')
    except:
        return return_problem_page(request)


def contract_monitor(request):
    try:
        arguments = {}
        arguments['contracts'] = Contract.objects.all()
        return render(request, 'smartpollution/contracts.html', arguments)
    except:
        return return_problem_page(request)

def return_problem_page(request):
    """
    This handels all problems and displays the problem page
    :param request: 
    :return: 
    """
    return render(request,'smartpollution/problem.html')
