
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