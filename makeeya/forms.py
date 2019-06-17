from django import forms
from django.contrib.auth.models import User
from .models import Profile, Item, Request

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['user','business_name','business_description']

class RequestForm(forms.ModelForm):
    class Meta:
        model = Request
        exclude = ['Request_date']

class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields= "__all__"
   


