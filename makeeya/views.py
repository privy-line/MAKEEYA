from django.shortcuts import render,redirect
from django.http  import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Profile,Request
from .forms import ProfileForm

# Create your views here.
def home(request):
  return render(request,'home.html')

def profile(request,id):
    request=Request.objects.get(id=id)
    profile=Profile.objects.get(user=current_user)
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            profile.business_name=form.cleaned_data['business_name']
            profile.business_description=form.cleaned_data['business_description']
            profile.business_logo = form.cleaned_data['business_logo']
            profile.business_email = form.cleaned_data['business_email']
            profile.business_address = form.cleaned_data['business_address']
            profile.user=current_user
            
            profile.save()
            return redirect(home)
    else:
        form = ProfileForm()
    return render(request, 'profile_form.html', {"form": form,'user':current_user})