from django import forms
from .models import Profile,Request

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'

class RequestForm(forms.ModelForm):
    class Meta:
        model = Request
        exclude = ['Request_date']
