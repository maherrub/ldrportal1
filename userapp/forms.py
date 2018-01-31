from django import forms
from django.forms.extras import SelectDateWidget
from django.contrib.auth.models import User
from functools import partial

#imports from local apps
from portal.choices import *
from userapp.models import *
from userapp.choices import *

#django-messages imports
#from django_messages.models import *
#from django_messages.forms import *


app_name = 'userapp'

DateInput = partial(forms.DateInput, {'class': 'form-control datepicker'})



class UserProfileForm(forms.ModelForm):
    
    firstname = forms.CharField(label = 'First Name',)
    lastname = forms.CharField(label = 'Last Name',)
    usercover = forms.FileField(label = 'Profile picture (jpg / png only)',)
    usermobile = forms.CharField(label = 'Mobile Number',)
    country = forms.CharField(label = 'Country',)
    postal_code = forms.CharField(label = 'Postal Code',)
    
    class Meta:
        
        model = UserProfile
       
        fields = [
            
            'firstname', 
            'lastname', 
            'usercover', 
            'usermobile',
            'country',
            'postal_code',
            
            ]


#Profile Managers User Profile Form
class PMUPForm(forms.ModelForm):
    dob = forms.DateField(widget=DateInput(), label = "Date of birth",)
    is_leader = forms.ChoiceField(choices = BOOLEAN_LIST,)
    class Meta:
        model = UserProfile

        fields = [
            'user',
           
            'firstname', 
            'lastname', 
            'usercover', 
            'usermobile',
            'country',
            'postal_code',
            'is_leader',
            'manager_name',
            'manager_type',
            'ticket_manager_name',
            'user_type',

        ]





