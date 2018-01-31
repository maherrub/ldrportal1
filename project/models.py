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


#helpdesk Imports
from helpdesk.choices import *

#project Imports
from project.choices import *

#definitions
app_name = 'project'

# models here.

class Ldrproject(models.Model):
    projectId = models.AutoField(primary_key=True)
    projectName = models.CharField(max_length=100, null=True, blank=True)
    plannedStartDate = models.DateField(null=True, blank=True)
    plannedEndDate = models.DateField(null=True, blank=True)
    projectStartDate = models.DateField(null=True, blank=True)
    projectEndDate = models.DateField(null=True, blank=True)
    projectStatus = models.CharField(max_length=20, choices=PROJECT_STATUS, default='')
    projectType = models.CharField(max_length=20, choices=PROJECT_TYPES, default='')
    projectDescription = models.TextField(blank=True,)
    projectManager = models.ForeignKey(User, editable=True,)
    firstCreateDate = models.DateField(auto_now_add=True,)
    projectEditedOn = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ["-projectEditedOn"]

    def __str__(self):
        return str(self.projectName)



class Ldrresource(models.Model):
    resourceID = models.AutoField(primary_key=True)
    resourceOrder = models.IntegerField()
    resourceName = models.CharField(max_length=25,)
    userId = models.CharField(max_length=30, null=True, blank=True)
    resourceRole = models.CharField(max_length=30, choices=RESOURCE_ROLE, default='') 
    resourceToProject = models.ForeignKey(Ldrproject)
    resourceDescription = models.TextField(blank=True,)
    resourceManager = models.ForeignKey(User,default=1, editable=True,)
    firstCreateDate = models.DateField(auto_now_add=True,)
    resourceEditedOn = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ["resourceOrder"]

    def __str__(self):
        return str(self.resourceToProject)+ ":" +(self.resourceName)


class Ldrprojectschedule(models.Model):
    scheduleID = models.AutoField(primary_key=True)
    project = models.ForeignKey(Ldrproject)
    scheduleOrder = models.IntegerField()
    workPackageName = models.TextField(blank=True,)
    hoursPerDay = models.IntegerField()
    numberOfDays = models.IntegerField(null=True, blank=True,)
    workpackageType = models.CharField(max_length=15, choices=WORKPACKAGE_TYPE, default='')
    scheduleManager = models.ForeignKey(User, editable=True,)
    scheduleStartDate = models.DateField(null=True, blank=True,)
    scheduleEndDate = models.DateField(null=True, blank=True,)
    firstCreateDate = models.DateField(auto_now_add=True,)
    scheduleEditedOn = models.DateTimeField(default=timezone.now)
    
    class Meta:
        ordering = ["scheduleOrder"]

    def __str__(self):
        return str(self.scheduleID)


class  Ldrscheduledactivity(models.Model):
    activityID = models.AutoField(primary_key=True)
    scheduleName = models.ForeignKey(Ldrprojectschedule)
    activityOrder = models.IntegerField()
    activityName = models.TextField(blank=True,)
    members = models.ForeignKey(Ldrresource, default='',)
    numberOfDays = models.IntegerField(null=True, blank=True,)
    activityStartDate = models.DateField(null=True, blank=True,)
    activityEndDate = models.DateField(null=True, blank=True,)
    activityManager = models.ForeignKey(User, editable=True,)
    firstCreateDate = models.DateField(auto_now_add=True,)
    activityEditedOn = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ["activityOrder"]

    def __str__(self):
        return str(self.activityID)+(self.avtivityName)


class projectRisk(models.Model):
    riskID = models.AutoField(primary_key=True)
    project = models.ForeignKey(Ldrproject, default='')
    riskOrder = models.IntegerField()
    riskFlag = models.CharField(max_length=25, choices=RISK_FLAG, default='')
    riskweight = models.CharField(max_length=10, choices=RISK_WEIGHT, default='')
    riskName = models.CharField(max_length=50, null=True, blank=True)
    riskDescription = models.TextField(blank=True,)
    riskMitigation = models.TextField(blank=True,)
    mittigationStatus = models.CharField(max_length=25, choices=MITTIGATION_STATUS, default='') 
    riskIdentifiedDate = models.DateField(null=True, blank=True)
    riskMittigatedDate = models.DateField(null=True, blank=True)
    firstCreateDate = models.DateField(auto_now_add=True,)
    riskEditedOn = models.DateTimeField(default=timezone.now) 

    class Meta:
        ordering = ["riskOrder"]

    def __str__(self):
        return str(self.riskID)+(self.riskName)

class ProjectManager(models.Model):
    pmID = models.AutoField(primary_key=True)
    pmUsername = models.CharField(max_length=40,)
    pmCreateDate = models.DateField(auto_now_add=True,)
    pmEditedOn = models.DateTimeField(default=timezone.now)
    

    def __str__(self):
        return str(self.pmUsername)











