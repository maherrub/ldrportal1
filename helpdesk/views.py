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
from django.db.models import Count
from django.db.models import Q
from django.core.paginator import Paginator


#local apps imports
from userapp.models import UserProfile
#helpdesk imports
from helpdesk.models import *
from helpdesk.forms import *


#definitions
app_name = 'helpdesk'


# Views here.
class TicketManagerCreate(CreateView):
    model = TicketManager
    form_class = TicketManagerForm
       
    def get_initial(self):
        initials = super(TicketManagerCreate, self).get_initial()
        initials['ticket_manager_ticket'] = self.kwargs['fg']
        return initials
    
    def get_success_url(self):
        pk = self.kwargs['fg']
        return reverse('helpdesk:ticket_detail', kwargs={'pk': pk})
        
class SupportTicketManagerCreate(CreateView):
    model = TicketManager
    form_class = SupportTicketManagerForm
    template_name = 'helpdesk/supportticketmanager_form.html'

    def get_initial(self):
        initials = super(SupportTicketManagerCreate, self).get_initial()
        initials['ticket_manager_ticket'] = self.kwargs['fg']
        return initials

    def get_success_url(self):
        pk = self.kwargs['fg']
        return reverse('helpdesk:supportticket_detail', kwargs={'pk': pk})

class TicketResolutionAdminCreate(CreateView):
    model = TicketResolution
    form_class = TicketResolutionAdminForm
    template_name = 'helpdesk/ticketresolutionadmin_form.html'

    def get_initial(self):
        initials = super(TicketResolutionAdminCreate, self).get_initial()
        initials['resolution_admin_ticket'] = self.kwargs['fg']
        return initials

    def get_success_url(self):
        pk = self.kwargs['fg']
        return reverse('helpdesk:supportticket_detail', kwargs={'pk': pk})




#class TicketList(ListView):
#    model = Ticket
#    paginate_by = 5

class UserTicketList(ListView):
    #model = Ticket
    context_object_name = 'user_object_list'
    #paginate_by = 5
    template_name = 'helpdesk/userticket_list.html'
    def get_queryset(self):
        qs = Ticket.objects.filter(ticket_owner=self.request.user)
        query = self.request.GET.get("q")
        if query:
            qs = qs.filter(
                Q(ticket_number__icontains=query)|
                Q(ticket_issue__icontains=query)|
                Q(ticket_status__icontains=query)|
                Q(ticket_description__icontains=query)|                
                Q(ticket_priority__icontains=query)|
                Q(first_create_date__contains=query)
                ).distinct()
        return qs

    def get_context_data(self, **kwarg):
        context = super(UserTicketList, self).get_context_data(**kwarg)
        context['object_list_all'] = Ticket.objects.exclude(user_group = "None")
        context['user_object_count'] = Ticket.objects.filter(ticket_owner=self.request.user).count()
        context['thisuprofile'] = UserProfile.objects.filter(user=self.request.user)
        context['uprofile'] = UserProfile.objects.all()
        return context


class ServiceTicketList(ListView):
    model = Ticket
    paginate_by = 20
    template_name = 'helpdesk/serviceticket_list.html'

    def get_context_data(self, **kwarg):
        context = super(ServiceTicketList, self).get_context_data(**kwarg)
        context['ticketmanager_list'] = TicketManager.objects.order_by('-ticket_manager_edited_on')
        context['contacts'] = User.objects.all()
        context['profiles'] = UserProfile.objects.all()      
        return context


class ManagerTicketList(ListView):
    model = Ticket
    paginate_by = 20
    template_name = 'helpdesk/managerticket_list.html'

    
    def get_context_data(self, **kwarg):
        context = super(ManagerTicketList, self).get_context_data(**kwarg)
        context['ticketmanager_list'] = TicketManager.objects.order_by('-ticket_manager_edited_on')
        context['ticket_list'] = Ticket.objects.order_by('-ticket_edited_on')
        context['contacts'] = User.objects.all()
        context['profiles'] = UserProfile.objects.all()      
        return context


class SupportTicketList(ListView):
    model = Ticket
    paginate_by = 20
    template_name = 'helpdesk/supportticket_list.html'

class UserTicketCreate(CreateView):
    model = Ticket
    form_class = UserTicketForm
    template_name = 'helpdesk/userticket_form.html'

    #send email when a new ticket is created
    def form_valid(self, form):
        
        form.instance.ticket_owner = self.request.user
        to_email = self.request.user.email

        subject = 'New support ticket has been created.'
        message = 'Hi, We have received your support ticket. Our service desk admin is looking in to your request. - LDR Service Desk'
    
        send_mail(subject, message, 'itservices@ldr.sg',
        ['itservices@ldr.sg', to_email,], fail_silently=False)
        
        return super(UserTicketCreate, self).form_valid(form)
    

#class TicketCreate(CreateView):
#    model = Ticket
#    form_class = TicketForm
    
 #   def dispatch(self, *args, **kwargs):
 #       return super(TicketCreate, self).dispatch(*args, **kwargs)
    
       

class UserTicketDetail(DetailView):
    model = Ticket
    template_name = 'helpdesk/userticket_detail.html'

    def get_context_data(self, **kwarg):
        context = super(UserTicketDetail, self).get_context_data(**kwarg)
        context['ticketmanager_list'] = TicketManager.objects.order_by('-ticket_manager_edited_on')
        context['resolutionadmin_list'] = TicketResolution.objects.order_by('-resolution_admin_edited_on')
        context['contacts'] = User.objects.get(username=self.request.user)
        context['profiles'] = UserProfile.objects.get(user=self.request.user)      
        return context

class ServiceTicketDetail(DetailView):
    model = Ticket
    template_name = 'helpdesk/serviceticket_detail.html'

    def get_context_data(self, **kwarg):
       
        context = super(ServiceTicketDetail, self).get_context_data(**kwarg)
        context['ticketmanager_list'] = TicketManager.objects.order_by('-ticket_manager_edited_on')
        context['contacts'] = User.objects.all()
        context['profiles'] = UserProfile.objects.all()       
        return context
        
class ManagerTicketDetail(DetailView):
    model = Ticket
    template_name = 'helpdesk/managerticket_detail.html'

    def get_context_data(self, **kwarg):
       
        context = super(ManagerTicketDetail, self).get_context_data(**kwarg)
        context['ticketmanager_list'] = TicketManager.objects.order_by('-ticket_manager_edited_on')
        context['contacts'] = User.objects.all()
        context['profiles'] = UserProfile.objects.all()       
        return context

class SupportTicketDetail(DetailView):
    model = Ticket
    template_name = 'helpdesk/supportticket_detail.html'

    def get_context_data(self, **kwarg):

        context = super(SupportTicketDetail, self).get_context_data(**kwarg)
        context['ticketmanager_list'] = TicketManager.objects.order_by('-ticket_manager_edited_on')
        context['resolutionadmin_list'] = TicketResolution.objects.order_by('-resolution_admin_edited_on')
        context['contacts'] = User.objects.all()
        context['profiles'] = UserProfile.objects.all()
        return context


#class TicketDetail(DetailView):
#    model = Ticket

#    def get_context_data(self, **kwarg):
       
#        context = super(TicketDetail, self).get_context_data(**kwarg)
#        context['ticketmanager_list'] = TicketManager.objects.order_by('-ticket_manager_edited_on')
#        context['contacts'] = User.objects.all()
#        context['profiles'] = UserProfile.objects.all()       
#        return context
        
class TicketManagerDetail(DetailView):
    model = TicketManager
    template_name = 'helpdesk/ticketmanager_detail.html'


#class TicketUpdate(UpdateView):
#    model = Ticket
#    form_class = TicketForm
#    template_name_suffix = '_update'


class UserTicketUpdate(UpdateView):
    model = Ticket
    form_class = UserTicketUpdateForm
    template_name = 'helpdesk/userticket_update.html'

    def get_success_url(self):
        pk = self.kwargs['pk']
        return reverse('helpdesk:userticket_detail', kwargs={"pk": pk})


class ServiceTicketUpdate(UpdateView):
    model = Ticket
    form_class = ServiceTicketForm
    template_name = 'helpdesk/serviceticket_update.html'
    
    def get_success_url(self):
        pk = self.kwargs['pk']
        return reverse('helpdesk:serviceticket_detail', kwargs={'pk': pk})

class ManagerTicketUpdate(UpdateView):
    model = Ticket
    form_class = ManagerTicketForm
    template_name = 'helpdesk/managerticket_update.html'
    
    def get_success_url(self):
        pk = self.kwargs['pk']
        return reverse('helpdesk:managerticket_detail', kwargs={'pk': pk})

class SupportTicketUpdate(UpdateView):
    model = Ticket
    form_class = SupportTicketForm
    template_name = 'helpdesk/supportticket_update.html'
    
    #send email when the status of the ticket is changed by the support admin
    def get_success_url(self):
        pk = self.kwargs['pk']
        this_ticket = Ticket.objects.get(ticket_number=pk)
        this_ticket_status = this_ticket.ticket_status
        this_owner = this_ticket.ticket_owner
        this_user = User.objects.get(username=this_owner)
        to_email = this_user.email

        subject = 'Your LDR support ticket number :' + pk + ' status has been changed'
        message = 'Hi, Your support ticket status has now been set to : ' + this_ticket_status + ' by the support admin. Please login to LDR Portal support ticket console and click your ticket detail button for more information.- LDR Support Admin'
    
        send_mail(subject, message, 'itservices@ldr.sg',
        [to_email,], fail_silently=False)
        
        return reverse('helpdesk:supportticket_detail',kwargs={'pk':pk})
        


class TicketManagerList(ListView):
    queryset = TicketManager.objects.order_by('-ticket_manager_edited_on')
    context_object_name = 'ticket_manager_list'

#def hd(request, self):
#    tickets = Ticket.objects.all()
#    replies = TicketManager.objects.all()
#    if request.user.is_authenticated():
#        uname = self.request.user
#    return render(request, 'helpdesk/ticket_manager_list.html', {'tickets': tickets, 'replies': replies, 'uname': uname, })

