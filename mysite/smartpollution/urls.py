from django.conf.urls import url

from . import views

from django.conf.urls import url

from . import views
from . import downloads
from . import db_manipulation

app_name = 'smartpollution'
urlpatterns = [
    url(r'^$', views.index_view, name='index'),
    url(r'^templates', views.index_template_view, name='index_templates'),
    url(r'^about', views.about_view, name='about'),
    url(r'^devices', views.device_search_view, name='device_search'),

    url(r'^registerdevice/$', views.register_device_view, name='register_device'),
    url(r'^registerdevice/add$', db_manipulation.add_device, name='register_device_add'),
    url(r'^registermetric/$', views.register_metric_view, name='register_metric'),
    url(r'^registermetric/add$', db_manipulation.add_metric, name='register_metric_add'),
    url(r'^registermetric/addSilent/(?P<pk>[0-9]+)/$', db_manipulation.add_metric_silent, name='register_metric_add_silent'),

    url(r'^device/(?P<pk>[0-9]+)/$', views.detail_view, name='detail'),

    url(r'^template/(?P<pk>[0-9]+)/$', views.detail_template_view, name='detail_template'),
    url(r'^template/(?P<pk>[0-9]+)/download$', downloads.send_smart_contract, name='download_smartcontract'),
    url(r'^template/(?P<pk>[0-9]+)/downloadthresholds$', downloads.send_smart_contract_thresholds, name='download_smartcontract_thresholds'),

    url(r'^device/(?P<pk>[0-9]+)/add_metric/$', db_manipulation.add_metric_to_device, name='add_metric_to_device'),

    url(r'^device/(?P<pk>[0-9]+)/addMetricSave/$', db_manipulation.save_metric_to_device,name='add_metric_to_device_save'),

    url(r'^device/(?P<pk>[0-9]+)/addTemplate/$', db_manipulation.add_template_to_device, name='add_template_to_device'),
    url(r'^device/(?P<pk>[0-9]+)/addTemplateSave/$', db_manipulation.save_template_to_device,name='add_template_to_device_save'),

    url(r'^cotracts$', views.contract_monitor,name='contract_monitor'),
    url(r'^contracts/(?P<pk>[0-9]+)/$', views.detail_contract_view, name='detail_contract'),

    url(r'^registercontract/$', views.register_contract_view, name='register_contract'),
    url(r'^registercontract/add$', db_manipulation.add_contract, name='register_contract_add'),

    url(r'^problem$', views.return_problem_page,name='problem'),
    url(r'.*', views.return_problem_page,name='do_not_use_this_only_for_error_handling'),
]
