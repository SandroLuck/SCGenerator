
# Create your models here.
from django.db import models
from django.utils import timezone
import datetime


class Metric(models.Model):
    physical_property=models.CharField(max_length=200)
    unit_of_measurement=models.CharField(max_length=200)

    def __str__(self):
        return self.physical_property+" in "+self.unit_of_measurement


#This is the datamodel for devices
class Device(models.Model):
    #maxlength of the string is 200 due to standartization
    device_name=models.CharField(max_length=200)
    manufacturing_company=models.CharField(max_length=200)
    metrics=models.ManyToManyField(Metric)
    def __str__(self):
        return self.device_name

class Template(models.Model):
    template_name=models.CharField(max_length=200, null=True)
    device=models.ForeignKey(Device, on_delete=models.CASCADE)
    def __str__(self):
        return str(self.template_name)


class Threshold(models.Model):
    template=models.ForeignKey(Template, on_delete=models.CASCADE)
    metric=models.ForeignKey(Metric, on_delete=models.CASCADE)
    lower_trigger=models.DecimalField( max_digits=19, decimal_places=10, blank=True, null=True)
    upper_trigger=models.DecimalField( max_digits=19, decimal_places=10, blank=True, null=True)
    def __str__(self):
        return str(self.id)

class Contract(models.Model):
    contract_name=models.CharField(max_length=200, null=True)
    contract_address=models.CharField(max_length=42, null=True)#42 since a contract address with 0x is len(add)=42 e.g. 0x3B03c46Dfc878FeF9fAe8de4E32a6718f2E250e9
    contract_abi=models.CharField(max_length=2000,null=True)
    def __str__(self):
        return str(self.contract_name)