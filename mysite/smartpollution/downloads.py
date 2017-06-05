import mimetypes
import os, tempfile, zipfile

from django.utils.text import slugify
from django.http import HttpResponse
from wsgiref.util import FileWrapper

from .generate_smartcontract import create_new_smart_contract
from django.shortcuts import render
from .models import Template, Threshold, Metric, Device


def send_smart_contract(request, pk):
    """                                                                         
    Create a smartcontract file on disk and transmit it.                
    """
    try:
        print("IN SEND_SAMART_COTNRA")
        templ = Template.objects.get(id=pk)
        print("IN SEND_SAMART_COTNRA2")
        temp_name = str(slugify(
            templ.template_name))
        # temp_lower = thres.lower_trigger
        # temp_upper = thres.upper_trigger
        mets = []
        device = Device.objects.get(id=Template.objects.get(id=pk).device_id)
        print("IN SEND_SAMART_COTNRA3"+str(device))

        mets_quarry = device.metrics.all()
        for met in mets_quarry:
            mets.append(str(met.physical_property)+str(met.unit_of_measurement))
        print("METS: " + str(mets))
        path = create_new_smart_contract(template_name=temp_name, metrics=mets)
        test_file = FileWrapper(open(path, 'rb'))
        print("IN SEND_SAMART_COTNRA2")

        response = HttpResponse(test_file, content_type='text/plain')
        response['Content-Disposition'] = r'attachment; filename=MyPollutionMonitoringContract.sol'
        os.remove(path)
        return response
    except:
        pass

"""def send_smart_contract(request, pk):
                                                                           
    Create a smartcontract file on disk and transmit it.                

    try:
        print("IN SEND_SAMART_COTNRA")
        templ = Template.objects.get(id=pk)
        thresholds = Threshold.objects.filter(template=Template.objects.get(id=pk))
        temp_name = str(slugify(
            templ.template_name + "For" + thres.metric.physical_property + "In" + thres.metric.unit_of_measurement))
        temp_metric = str(slugify(thres.metric.physical_property + "In" + thres.metric.unit_of_measurement))
        # temp_lower = thres.lower_trigger
        # temp_upper = thres.upper_trigger
        mets = []
        device = Device.objects.get(id=Template.objects.get(id=pk).device_id)
        mets = device.metrics
        print("METS: " + mets)
        path = create_new_smart_contract(template_name=temp_name, metrics=mets)
        test_file = FileWrapper(open(path, 'rb'))

        response = HttpResponse(test_file, content_type='text/plain')
        response['Content-Disposition'] = r'attachment; filename=MyPollutionMonitoringContract.sol'
        os.remove(path)
        return response
    except:
        pass"""