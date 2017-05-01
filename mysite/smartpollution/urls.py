from django.conf.urls import url

from . import views

from django.conf.urls import url

from . import views

app_name = 'smartpollution'
urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),

    url(r'^css/form.css$', views.RegisterDeviceView.as_view(), name='css'),

    url(r'^registerdevice/$', views.RegisterDeviceView.as_view(), name='register_device'),
    url(r'^registerdevice/add$', views.addDevice, name='register_device_add'),
    url(r'^registermetric/$', views.RegisterMetricView.as_view(), name='register_metric'),
    url(r'^registermetric/add$', views.addMetric, name='register_metric_add'),
    url(r'^device/(?P<pk>[0-9]+)/$', views.DetailView, name='detail'),

    url(r'^template/(?P<pk>[0-9]+)/$', views.DetailViewTemplate, name='detail_template'),

    url(r'^device/(?P<pk>[0-9]+)/addMetric/$', views.AddMetricToDevice, name='add_metric_to_device'),
    url(r'^device/(?P<pk>[0-9]+)/addMetricSave/$', views.saveMetricToDevice, name='add_metric_to_device_save'),

    url(r'^device/(?P<pk>[0-9]+)/addTemplate/$', views.AddTemplateToDevice, name='add_template_to_device'),
    url(r'^device/(?P<pk>[0-9]+)/addTemplateSave/$', views.saveTemplateToDevice, name='add_template_to_device_save'),
]