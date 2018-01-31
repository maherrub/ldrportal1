from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from project.views import *

app_name = 'project'

urlpatterns = [
    #url(r'^hd/$', hd, name='hd'),
    url(r'^projectorg_list/$', ProjectOrgList.as_view(), name='projectorg_list'),
    url(r'^projectticket_list/$', ProjectTicketList.as_view(), name='projectticket_list'),
    url(r'^resource_tickets/(?P<rk>[\w-]+)/(?P<fk>[\w-]+)/$', ProjectTicketList.as_view(), name='resource_tickets',),
    url(r'^resource_fullticket_list/(?P<fk>[\w-]+)/$', ProjectTicketFullList.as_view(), name='resource_fullticket_list',),

    url(r'^(?P<pk>[-\w]+)/projectorg_detail$', ProjectOrgDetail.as_view(), name='projectorg_detail'),
    url(r'^(?P<pk>[-\w]+)/schedule_activity_detail$', ScheduleActivityDetail.as_view(), name='schedule_activity_detail'),

    
]
urlpatterns = format_suffix_patterns(urlpatterns)