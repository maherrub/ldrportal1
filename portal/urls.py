from django.conf.urls import include, url
from django.contrib import admin
from django.conf.urls.i18n import i18n_patterns
from django.utils.translation import activate
from portal.views import *

app_name = 'portal'

urlpatterns = [
    
    url(r'^$', HomeView.as_view(), name='home',),
    url(r'^apps_list/$', AppsView.as_view(), name='apps_list',),
    
]