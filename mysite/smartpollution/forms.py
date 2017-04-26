from django import forms
from smartpollution.models import Metric

class RegisterDeviceForm(forms.Form):
    device_name = forms.CharField()
    manufacturing_company = forms.CharField()

class RegisterMetricForm(forms.Form):
    physical_property = forms.CharField()
    unit_of_measurement = forms.CharField()

class AddMetricsToDeviceForm(forms.Form):
    all_metrics=[]
    for metric in Metric.objects.all():
        all_metrics.append((metric.id, metric.physical_property+' in '+metric.unit_of_measurement ))
    Metrics=forms.MultipleChoiceField(choices=all_metrics, widget=forms.CheckboxSelectMultiple)