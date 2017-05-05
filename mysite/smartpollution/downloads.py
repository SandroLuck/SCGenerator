import mimetypes
import os, tempfile, zipfile
from django.http import HttpResponse
from wsgiref.util import FileWrapper

from django.shortcuts import render


def send_smart_contract(request, pk):
    """                                                                         
    Create a smartcontract file on disk and transmit it.                
    """
    try:
        path=r"C:\Users\sandr\Desktop\smartContractExample.sol"
        test_file = FileWrapper(open(path, 'rb'))
        response = HttpResponse(test_file ,content_type='text/plain')
        response['Content-Disposition'] = r'attachment; filename=smartContractExample.sol'
        return response
    except:
        pass
