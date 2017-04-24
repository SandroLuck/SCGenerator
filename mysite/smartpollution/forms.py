from django import forms

class RegisterDeviceForm(forms.Form):
    device_name = forms.CharField()
    manufacturing_company = forms.CharField()

class RegisterMetricForm(forms.Form):
    physical_property = forms.CharField()
    unit_of_measurement = forms.CharField()

