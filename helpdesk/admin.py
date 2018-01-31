from django.contrib import admin
from django.contrib.admin.widgets import AdminTextInputWidget, AdminTextareaWidget
from helpdesk.models import *
from helpdesk.choices import *

# Register your models here.

class SupportAdministratorAdmin(admin.ModelAdmin):
    fields = ['functional_group', 'functional_subgroup', 'administrator',]
    list_display = ['functional_group', 'functional_subgroup', 'administrator', ]
    
       

class TicketAdmin(admin.ModelAdmin):
    
    fields = ['attach2project', 'ticket_category', 'ticket_issue', 'ticket_priority', 'ticket_status', 'ticket_screenshot', 'ticket_description', 'ticket_owner', 'consent_manager_key', 'consent_manager_name', 'user_group', 'consent_manager_signed', 'assigned_admin', 'ticket_edited_on',]
    list_display = ['attach2project', 'ticket_category', 'ticket_number', 'ticket_owner', 'ticket_issue', 'ticket_priority', 'ticket_status', 'consent_manager_name', 'user_group', 'consent_manager_signed', 'assigned_admin',]
    list_editable = ['attach2project', 'ticket_priority', 'ticket_status', 'assigned_admin', 'consent_manager_signed',]
    list_filter = ['attach2project', 'ticket_category', 'ticket_number', 'ticket_priority', 'ticket_status', 'ticket_owner', 'user_group', 'ticket_edited_on',]
    search_fields = ['ticket_number', 'ticket_description', 'ticket_owner',]



#class TicketManagerAdmin(admin.ModelAdmin):
#    fields = ['ticket_manager_ticket', 'ticket_manager_fg', 'ticket_manager_reply', 'ticket_manager_name',]
#    list_display = ['ticket_manager_fg', 'ticket_manager_reply', 'ticket_manager_ticket', 'ticket_manager_edited_on', 'ticket_manager_name']
    


class TicketResolutionAdmin(admin.ModelAdmin):
    fields = ['resolution_admin_ticket', 'resolution_admin_fg', 'resolution_admin_reply', 'resolution_admin_name',]
    list_display = ['resolution_admin_fg', 'resolution_admin_reply', 'resolution_admin_ticket', 'resolution_admin_edited_on', 'resolution_admin_name',]

admin.site.register(SupportAdministrator, SupportAdministratorAdmin)
#admin.site.register(TicketManager, TicketManagerAdmin)
admin.site.register(TicketResolution, TicketResolutionAdmin)
admin.site.register(Ticket, TicketAdmin)
