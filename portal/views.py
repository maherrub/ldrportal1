from django.shortcuts import render, redirect
from django.shortcuts import render_to_response
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate 
from django.contrib.auth import login 
from django.contrib.auth import logout
from django.http import HttpRequest
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
from django.db.models import Count
from django.utils.safestring import mark_safe
from django.db.models import Q

#localapp imports
from userapp.models import *
from helpdesk.models import *
from project.models import *


#portal imports
from portal.models import *
from portal.choices import *
#from portal.forms import *


#django-messages imports
#from django_messages.models import *
#from django_messages.forms import *

#definitions
app_name = 'portal'

#pagination libraries
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


#date time definitions
from datetime import *


today = date.today()
yesterday = today - timedelta(1)
last7day = today - timedelta(7)
last31day = today - timedelta(31)
last31dayo = last7day - timedelta(31) 
last365day = today - timedelta(365)

# All Views here.

class HomeView(ListView):
    context_object_name = 'home'
    template_name ='portal/index.html'
    queryset = User.objects.all()

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        context['uprofile'] = UserProfile.objects.all().distinct()
        return context
    
    #return render(request, ['portal/index.html'],)
    #return render(request, ['portal/index.html'], {'hgmall':hgmall, })

#Apps Store
class AppsView(ListView):
    context_object_name = 'user_list'
    template_name ='apps.html'
    queryset = User.objects.all()

    def get_context_data(self, **kwargs):
        context = super(AppsView, self).get_context_data(**kwargs)
        context['hgmall'] = HomeGroupManager.objects.all().filter(hgp_manager_name = self.request.user).distinct() #homegroup managers
        context['pms'] = ProfileManager.objects.all().filter(pm_manager_name = self.request.user).distinct() #profile managers
        context['ups'] = UserProfile.objects.filter(user = self.request.user).distinct() #get current user profile
        context['ups_today'] = UserProfile.objects.filter(created__gte = today)
        context['stas'] = SupportAdministrator.objects.filter(administrator = self.request.user).distinct() #support ticket admins
        context['ticket_list'] = Ticket.objects.filter(first_create_date__gte = last31day) 
        context['usertickets_change'] = Ticket.objects.filter(last_modified_date__gte = today)
        context['reply24'] = Ticket.objects.filter(last_modified_date__gte = yesterday ) 
        context['usertickets_last1day'] = TicketResolution.objects.filter(last_modified_date__gte = yesterday )
        context['usertickets_last7day'] = TicketResolution.objects.filter(last_modified_date__gte = last7day )
        context['uprofile'] = UserProfile.objects.filter(pk = self.request.user.id).distinct()
        context['projectmanager'] = ProjectManager.objects.all().filter(pmUsername = self.request.user).distinct()
        return context  
