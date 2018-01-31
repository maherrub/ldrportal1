from __future__ import unicode_literals
from django.db import models
import datetime
from django.utils import timezone
from django.core.urlresolvers import reverse
from multiselectfield import MultiSelectField
#from datetime import *

#local apps Imports
from django.contrib.auth.models import User
from userapp.models import UserProfile
from project.models import Ldrproject

#helpdesk Imports
from helpdesk.choices import *

#definitions
app_name = 'helpdesk'

# models here.
#Changed from HelpDeskManager to SupportAdministrator
#class HelpDeskManager(models.Model):
#    hdmgr_functional_group = models.CharField(max_length=25, choices=HDMGR_FUNCTIONAL_GROUP_LIST)
#    hdmgr_functional_group_area = models.CharField(max_length=75,)
#    hdmgr_ticket_manager_name = models.CharField(max_length=50,)

#    def __str__(self):
#        return str(self.hdmgr_functional_group + '-' + self.hdmgr_functional_group_area + '-' + self.hdmgr_ticket_manager_name)

class SupportAdministrator(models.Model):
    functional_group = models.CharField(max_length=25, choices=FUNCTIONAL_GROUP_LIST)
    functional_subgroup = models.CharField(max_length=75,)
    administrator = models.CharField(max_length=50,)

    def __str__(self):
        return str(self.administrator)
        #return str(self.functional_group + '-' + self.functional_subgroup + '-' + self.administrator)




#assigned_manager has been changed to assigned_admin 20180101
class Ticket(models.Model):
    ticket_number = models.AutoField(primary_key=True)
    ticket_category = models.CharField(max_length=50, choices=TICKET_CATEGORY_LIST,)
    ticket_issue = models.CharField(max_length=100, null=True, blank=True)
    ticket_priority = models.CharField(max_length=25, choices=TICKET_PRIORITY_LIST, default='Normal')
    ticket_status = models.CharField(max_length=25, choices=TICKET_STATUS_LIST, default='Started')
    ticket_description = models.TextField(blank=True,)
    ticket_screenshot = models.FileField(upload_to='helpdesk_snapshots/', null=True, blank=True)
    ticket_owner = models.ForeignKey(User, editable=True,)
    consent_manager_key = models.ForeignKey(UserProfile, default=1)
    consent_manager_name = models.CharField(max_length=20,null=True, blank=True)
    user_group = models.CharField(max_length=20,null=True, blank=True)
    consent_manager_signed = models.CharField(max_length=25,choices=TICKET_APPROVAL_CHOICE, default='', null=True, blank=True )
    consent_manager_reason = models.TextField(null=True, blank=True,)
    assigned_admin = models.ForeignKey(SupportAdministrator, default=1,)
    attach2project = models.ForeignKey(Ldrproject, null=True, blank=True,)
    first_create_date = models.DateField(auto_now_add=True,)
    last_modified_date = models.DateField(auto_now=True,) 
    ticket_edited_on = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ["-ticket_edited_on"]
    
    def save(self, *args, **kwargs):
        
        self.consent_manager_name = self.consent_manager_key.ticket_manager_name
        self.user_group = self.consent_manager_key.user_group
        super(Ticket, self).save(*args, **kwargs)
        
        
        """
        self.consent_manager_name = self.consent_manager_key.ticket_manager_name
        super(Ticket, self).save(*args, **kwargs)

        """


    
    def get_absolute_url(self):
        return reverse("helpdesk:userticket_detail", kwargs={"pk": self.pk})
       

    def __str__(self):
        return str(self.ticket_number)



class TicketManager(models.Model):
    ticket_manager_ticket = models.ForeignKey(Ticket)
    ticket_manager_fg = models.ForeignKey(SupportAdministrator)
    ticket_manager_reply = models.TextField(blank=True,)
    ticket_manager_name = models.ForeignKey(User, default=1)
    first_create_date = models.DateField(auto_now_add=True,)
    last_modified_date = models.DateField(auto_now=True,)
    ticket_manager_edited_on = models.DateTimeField(default=timezone.now)

    def get_absolute_url(self):
        return reverse("helpdesk:ticketmanager_detail", kwargs={"pk": self.pk})
        #return reverse('helpdesk:ticketmanager_detail', args={'pk': str[self.pk]})

    def __str__(self):
        return str(self.ticket_manager_ticket)


class TicketResolution(models.Model):
    resolution_admin_ticket = models.ForeignKey(Ticket)
    resolution_admin_fg = models.ForeignKey(SupportAdministrator)
    resolution_admin_reply = models.TextField(blank=True,)
    resolution_admin_name = models.ForeignKey(User, default=1)
    first_create_date = models.DateField(auto_now_add=True,)
    last_modified_date = models.DateField(auto_now=True,)
    resolution_admin_edited_on = models.DateTimeField(default=timezone.now)

    def get_absolute_url(self):
        return reverse("helpdesk:ticketmanager_detail", kwargs={"pk": self.pk})
        
    def __str__(self):
        return str(self.ticket_admin_ticket)






    
