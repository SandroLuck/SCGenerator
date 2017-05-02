from django.conf.urls import url

from . import views

from django.conf.urls import url

from . import views

app_name = 'smartpollution'
urlpatterns = [
    url(r'^$', views.IndexView, name='index'),
    url(r'^templates', views.IndexTemplateView, name='index_templates'),
    url(r'^about', views.AboutView, name='about'),

    url(r'^registerdevice/$', views.RegisterDeviceView, name='register_device'),
    url(r'^registerdevice/add$', views.addDevice, name='register_device_add'),
    url(r'^registermetric/$', views.RegisterMetricView, name='register_metric'),
    url(r'^registermetric/add$', views.addMetric, name='register_metric_add'),
    url(r'^device/(?P<pk>[0-9]+)/$', views.DetailView, name='detail'),

    url(r'^template/(?P<pk>[0-9]+)/$', views.DetailViewTemplate, name='detail_template'),

    url(r'^device/(?P<pk>[0-9]+)/addMetric/$', views.AddMetricToDevice, name='add_metric_to_device'),
    url(r'^device/(?P<pk>[0-9]+)/addMetricSave/$', views.saveMetricToDevice, name='add_metric_to_device_save'),

    url(r'^device/(?P<pk>[0-9]+)/addTemplate/$', views.AddTemplateToDevice, name='add_template_to_device'),
    url(r'^device/(?P<pk>[0-9]+)/addTemplateSave/$', views.saveTemplateToDevice, name='add_template_to_device_save'),
]