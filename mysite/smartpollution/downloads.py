import mimetypes
import os, tempfile, zipfile

from django.utils.text import slugify
from django.http import HttpResponse
from wsgiref.util import FileWrapper



from .generate_smartcontract import create_new_smart_contract
from django.shortcuts import render
from .models import Template, Threshold


def send_smart_contract(request, pk):
    """                                                                         
    Create a smartcontract file on disk and transmit it.                
    """
    try:
        templ=Template.objects.get(id=pk)
        thresholds=Threshold.objects.filter(template=Template.objects.get(id=pk))
        for thres in thresholds:
            temp_name=str(slugify(templ.template_name + "For" + thres.metric.physical_property + "In" + thres.metric.unit_of_measurement))
            temp_metric=str(slugify(thres.metric.physical_property + "In" + thres.metric.unit_of_measurement))
            temp_lower=thres.lower_trigger
            temp_upper=thres.upper_trigger
            path=create_new_smart_contract(template_name=temp_name, metric_name=temp_metric, lower_trigger=temp_lower, upper_trigger=temp_upper)
            test_file = FileWrapper(open(path, 'rb'))

            response = HttpResponse(test_file ,content_type='text/plain')
            response['Content-Disposition'] = r'attachment; filename=MyPollutionMonitoringContract.sol'
            os.remove(path)
        return response
    except:
        pass
