from django.db import models
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.utils import timezone
from django.core.validators import URLValidator

#portal application imports.
from portal.choices import *
from .validators import *

#definitions
app_name = 'portal'

# Create your models here.
class HomeGroupManager(models.Model):
    hgp_functional_group = models.CharField(max_length=25, choices=HG_FUNCTION_GROUP_LIST)
    hgp_manager_name = models.CharField(max_length=50,)
    added = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated = models.DateTimeField(auto_now=True, null=True, blank=True)

    def __str__(self):
        return str(self.hgp_manager_name)
