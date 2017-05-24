from django.contrib import admin

from .models import *

admin.site.register(Device)
admin.site.register(Metric)
admin.site.register(Template)
admin.site.register(Threshold)
admin.site.register(Contract)
