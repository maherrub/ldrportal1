from __future__ import unicode_literals
from django.core.urlresolvers import reverse
from django.contrib.auth.models import Permission, User
from multiselectfield import MultiSelectField
from django.db import models
from django.utils import timezone
from django.utils.encoding import python_2_unicode_compatible


#Local apps imports
from portal.choices import *
from portal.validators import *
from userapp.choices import *


#definitions
app_name = 'userapp'

#models.

class UserProfile(models.Model):
       
    user = models.ForeignKey(User, default=1)
    firstname = models.CharField(max_length=25, blank=True)
    lastname = models.CharField(max_length=25, blank=True)
    usercover = models.FileField(upload_to='uploads/profile_pictures/', validators=[validate_imagefile_extension], null=True, blank=True)
    usermobile = models.CharField(max_length=15, blank=True)
    country = models.CharField(max_length=20, blank=True)
    postal_code = models.CharField(max_length=7, blank=True)
    is_leader = models.BooleanField(default=False,)
    manager_name = models.CharField(max_length=20, blank=True)
    ticket_manager_name = models.CharField(max_length=20, default='ticketmanager')
    manager_type = models.CharField(max_length=20, choices=MANAGER_TYPE_LIST, blank=True)
    user_type = models.CharField(max_length=20, choices=USER_TYPE_LIST, default='External')
    user_group = models.CharField(max_length=20, choices=USER_GROUP_LIST, default='None')
    updated = models.DateTimeField(auto_now=True, null=True, blank=True)
    created = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.user.username

    def get_absolute_url(self):
        return reverse('userapp:detail', kwargs={'pk': self.pk})


@python_2_unicode_compatible
class ProfileManager(models.Model):
    pm_functional_group = models.CharField(max_length=25, choices=HG_FUNCTION_GROUP_LIST)
    pm_manager_name = models.CharField(max_length=50,)
    updated = models.DateTimeField(auto_now=True, null=True, blank=True)
    created = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return str(self.pm_manager_name)

@python_2_unicode_compatible
class FriendsList(models.Model):
    friend = models.ForeignKey(User, default=1)
    friendoffriend = models.CharField(max_length=150, null=True, blank=True,)
    frnd_options = models.CharField(max_length=25, choices=FRIENDS_LIST_OPTIONS)
    requested_date = models.DateTimeField(auto_now=True, null=True, blank=True,)
    frndoffrnd_options = models.CharField(max_length=25, choices=FRIENDS_LIST_OPTIONS)
    accepted_date = models.DateTimeField(auto_now=True, null=True, blank=True,)

    def __str__(self):
        return str(self.friend)


