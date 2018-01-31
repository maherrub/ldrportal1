from django.shortcuts import render
from django.conf import settings
from django.contrib import messages
from django.core.mail import send_mail
from django.core.mail import EmailMessage

from email.header import Header

from django.contrib.auth.models import User
from django.contrib.auth import authenticate 
from django.contrib.auth import login 
from django.contrib.auth import logout
from django.http import HttpRequest 
from django.shortcuts import render, redirect
from django.views.generic.list import ListView

from django.views.generic.base import RedirectView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required, permission_required
from django.utils.decorators import method_decorator
from django.utils import timezone
from django.core.urlresolvers import reverse_lazy
from multiselectfield import MultiSelectField

# Create your views here.

#local apps imports
from django.contrib.auth.models import User
from userapp.models import UserProfile
from helpdesk.models import *
from project.models import *

#helpdesk imports
from helpdesk.models import *
from helpdesk.forms import *


#definitions
app_name = 'project'

#List Views

class ProjectOrgList(ListView):
    model = Ldrproject
    paginate_by = 20
    template_name = 'project/projectorg_list.html'

    
    def get_context_data(self, **kwarg):
        context = super(ProjectOrgList, self).get_context_data(**kwarg)
        context['project_list'] = Ldrproject.objects.order_by('-projectEditedOn')
        #context['risk_list'] = projectRisk.objects.order_by('riskOrder')
        #context['resource_list'] = Ldrresource.objects.order_by('resourceOrder')
        #context['schedule_list'] = Ldrprojectschedule.objects.order_by('scheduleOrder')
        #context['activity_list'] = Ldrscheduledactivity.objects.order_by('activityOrder')
        context['member'] = User.objects.filter(is_staff = 1)
        context['profiles'] = UserProfile.objects.all()      
        return context

class ProjectTicketList(ListView):
    model = SupportAdministrator
    paginate_by = 20
    template_name = 'project/projectorg_ticket_list.html'

    def get_context_data(self, **kwarg):
        context = super(ProjectTicketList, self).get_context_data(**kwarg)
        context['supportadmin_list'] = SupportAdministrator.objects.filter(administrator = self.kwargs['fk'])
        context['ticket_list'] = Ticket.objects.order_by('-ticket_edited_on')
        context['resource_list'] = Ldrresource.objects.filter(resourceToProject = self.kwargs['rk'])
        context['project_list'] = Ldrproject.objects.filter(projectId = self.kwargs['rk'])
        context['member'] = User.objects.filter(is_staff = 1)
        context['profiles'] = UserProfile.objects.all()      
        return context


class ProjectTicketFullList(ListView):
    model = SupportAdministrator
    paginate_by = 20
    template_name = 'project/projectorg_fullticket_list.html'

    def get_context_data(self, **kwarg):
        context = super(ProjectTicketFullList, self).get_context_data(**kwarg)
        context['supportadmin_fulllist'] = SupportAdministrator.objects.filter(administrator = self.kwargs['fk'])
        context['ticket_fulllist'] = Ticket.objects.order_by('-ticket_edited_on')
        context['resource_fulllist'] = Ldrresource.objects.order_by('resourceOrder')
        context['project_fulllist'] = Ldrproject.objects.order_by('-projectEditedOn')
        context['member_fulllist'] = User.objects.filter(is_staff = 1)
        context['profiles_fulllist'] = UserProfile.objects.all()      
        return context





"""
    def get_queryset(self, **kwargs):
        qs = super(ProjectTicketList, self).get_queryset()
        qs1 = qs.filter(administrator = self.kwargs['fk'])
        qs2 = Ldrresource.objects.filter(resourceToProject = self.kwargs['rk'])
        return qs1, qs2
"""


"""
#producer home group parallax image list
class PHgPiList(ListView):
    model = HomeGroupParallaxImage
    template_name = 'website/phgpi_list.html'
    paginate_by = 20

    def get_queryset(self):
        qs = super(PHgPiList, self).get_queryset()
        return qs.filter(functional_group__exact=self.kwargs['fg'], hgpi_owner=self.request.user).distinct()

url(r'^phgpi_list/(?P<fg>[\w-]+)/$', PHgPiList.as_view(), name='phgpi_list',),


"""




#Detail Views
class ProjectOrgDetail(DetailView):
    model = Ldrproject
    template_name = 'project/projectorg_detail.html'

    def get_context_data(self, **kwarg):
        context = super(ProjectOrgDetail, self).get_context_data(**kwarg)
        context['project_list'] = Ldrproject.objects.order_by('-projectEditedOn')
        context['risk_list'] = projectRisk.objects.order_by('riskOrder')
        context['resource_list'] = Ldrresource.objects.order_by('resourceOrder')
        context['schedule_list'] = Ldrprojectschedule.objects.order_by('scheduleOrder')
        context['activity_list'] = Ldrscheduledactivity.objects.order_by('activityOrder')
        context['member'] = User.objects.filter(is_staff = 1)
        context['profiles'] = UserProfile.objects.all()      
        return context

class ScheduleActivityDetail(DetailView):
    model = Ldrprojectschedule
    template_name = 'project/scheduleactivity_detail.html'

    def get_context_data(self, **kwarg):
        context = super(ScheduleActivityDetail, self).get_context_data(**kwarg)
        context['schedule_list'] = Ldrprojectschedule.objects.order_by('scheduleOrder')
        context['activity_list'] = Ldrscheduledactivity.objects.order_by('activityOrder')
        context['member'] = User.objects.filter(is_staff = 1)
        context['profiles'] = UserProfile.objects.all()      
        return context




