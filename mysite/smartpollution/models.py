
# Create your models here.
from django.db import models
from django.utils import timezone
import datetime

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now

    def __str__(self):
        return self.question_text


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text

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
    template_name=models.CharField
    device=models.ForeignKey(Device, on_delete=models.CASCADE)
    def __str__(self):
        return self.template_name+", for device:"+Device.objects.get(self.device_id).device_name+" Device_id:"+self.device_id


class Threshold(models.Model):
    template=models.ForeignKey(Template, on_delete=models.CASCADE)
    metric=models.ForeignKey(Metric, on_delete=models.CASCADE)
    lower_trigger=models.DecimalField( max_digits=19, decimal_places=10)
    upper_trigger=models.DecimalField( max_digits=19, decimal_places=10)
    def __str__(self):
        return "Device:"+self.device_id+" Metric:"+self.metric_id+" Id treshold"+self.id
