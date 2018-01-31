from tastypie.resources import ModelResource,  ALL, ALL_WITH_RELATIONS
from django.contrib.auth.models import User
from tastypie.authorization import Authorization
from tastypie.authentication import BasicAuthentication

from itertools import chain
from operator import attrgetter

#apps import
from helpdesk.models import Ticket
from userapp.models import UserProfile
from project.models import Ldrproject


queryset1 = Ticket.objects.all()
queryset2 = UserProfile.objects.all()
queryset3 = Ldrproject.objects.all()

class TicketResource(ModelResource):
    class Meta:
        queryset = Ticket.objects.all()
        
        resource_name = 'ticket'
        """
        fields =    ['ticket_number', 
                    'ticket_category', 
                    'ticket_issue',
                    'ticket_priority',
                    'ticket_status',
                    'ticket_description',
                    'ticket_owner',
                    'consent_manager_name',
                    'consent_manager_signed',
                    'consent_manager_reason',
                    'assigned_admin',
                    'attach2project',
                    'first_create_date',
                    'last_modified_date',
                    'ticket_edited_on',
                    ]
        #excludes = ['']
        """
        authentication = BasicAuthentication()
        authorization = Authorization()

class LdrprojectResource(ModelResource):
    class Meta:
        queryset = Ldrproject.objects.all()
        resource_name = 'project'

        authentication = BasicAuthentication()
        authorization = Authorization()






