from django.contrib import admin
from django.contrib.admin.widgets import AdminTextInputWidget, AdminTextareaWidget
from project.models import *
from project.choices import *
# Register your models here.


class LdrprojectAdmin(admin.ModelAdmin):
    fields = ['projectName', 'plannedStartDate', 'plannedEndDate', 'projectStatus', 'projectType', 'projectStartDate', 'projectEndDate', 'projectDescription', 'projectManager', ]
    list_display = ['projectName', 'projectType', 'projectStatus', 'plannedStartDate', 'plannedEndDate', 'projectStartDate', 'projectEndDate', 'projectManager','projectEditedOn',]
    list_editable = ['projectStatus',]
    list_filter = ['projectType', 'projectStatus', 'projectStartDate', 'projectEndDate','projectManager',]
    search_fields = ['projectName', 'projectDescription',]

class LdrresourceAdmin(admin.ModelAdmin):
    fields = ['resourceOrder', 'resourceName', 'resourceRole', 'userId', 'resourceToProject', 'resourceDescription', 'resourceManager', ]
    list_display = ['resourceName', 'resourceOrder',  'resourceRole', 'resourceToProject', 'resourceEditedOn', ]
    list_editable = ['resourceOrder',]
    list_filter = ['resourceToProject', 'resourceName', 'resourceManager',]
    search_fields = ['resourceToProject',]

class LdrprojectscheduleAdmin(admin.ModelAdmin):
    fields = ['project', 'scheduleOrder', 'workPackageName', 'hoursPerDay', 'numberOfDays', 'workpackageType', 'scheduleManager', 'scheduleStartDate', 'scheduleEndDate', 'scheduleEditedOn', ]
    list_display = ['workPackageName', 'scheduleOrder',  'numberOfDays', 'workpackageType', 'scheduleStartDate', 'scheduleEndDate', 'scheduleEditedOn',]
    list_editable = ['scheduleOrder',]
    list_filter = ['project', 'workpackageType', 'scheduleStartDate', 'scheduleEndDate',]
    search_fields = []

class LdrscheduledactivityAdmin(admin.ModelAdmin):
    fields = ['scheduleName', 'activityOrder', 'activityName', 'members', 'numberOfDays', 'activityStartDate', 'activityEndDate', 'activityManager', 'activityEditedOn',]
    list_display = ['scheduleName', 'activityOrder', 'activityName', 'members', 'numberOfDays', 'activityStartDate', 'activityEndDate', 'activityEditedOn',]
    list_editable = ['activityOrder',]
    list_filter = ['activityName',  'activityStartDate', 'activityEndDate',]
    search_fields = ['members',]

class projectRiskAdmin(admin.ModelAdmin):
    fields = ['project', 'riskOrder', 'riskFlag', 'riskweight', 'riskName',  'riskDescription', 'riskMitigation', 'mittigationStatus', 'riskIdentifiedDate', 'riskMittigatedDate', ]
    list_display = ['riskName','riskOrder','riskFlag', 'riskweight', 'riskEditedOn', 'mittigationStatus', 'riskIdentifiedDate','riskMittigatedDate',]
    list_editable = []
    list_filter = ['project', 'riskweight',]
    search_fields = []

class ProjectManagerAdmin(admin.ModelAdmin):
    fields = ['pmUsername', 'pmEditedOn',]
    list_display = ['pmUsername', 'pmCreateDate', 'pmEditedOn',]
    list_editable = []
    list_filter = ['pmUsername', 'pmCreateDate', 'pmEditedOn',]
    search_fields = []

admin.site.register(Ldrproject, LdrprojectAdmin)
admin.site.register(Ldrresource, LdrresourceAdmin)
admin.site.register(Ldrprojectschedule, LdrprojectscheduleAdmin)
admin.site.register(Ldrscheduledactivity, LdrscheduledactivityAdmin)
admin.site.register(projectRisk, projectRiskAdmin)
admin.site.register(ProjectManager, ProjectManagerAdmin)

