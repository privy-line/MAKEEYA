from django import forms
from django.contrib.auth.models import User
from .models import Profile, Item, Request


class RequestForm(forms.ModelForm):
    class Meta:
        model = Request
        exclude = ['Request_date']

class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields= "__all__"
   


