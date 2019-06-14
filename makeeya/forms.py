from django import forms
<<<<<<< HEAD
from .models import Profile,Request

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'
=======
from django.contrib.auth.models import User
from .models import Profile, Item, Request

>>>>>>> origin

class RequestForm(forms.ModelForm):
    class Meta:
        model = Request
        exclude = ['Request_date']
<<<<<<< HEAD
=======

class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields= "__all__"
   


>>>>>>> origin
