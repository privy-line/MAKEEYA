from django.shortcuts import render,redirect
<<<<<<< HEAD
from django.http  import HttpResponse
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from .models import Profile,Request
from .forms import ProfileForm,RequestForm
from .email import send_notification_email
=======
from django.http  import HttpResponse,HttpResponseRedirect
from .forms import RequestForm
from django.contrib import messages
from .models import Buyer,Profile, Request, Category
from .email import send_notification_email
from django.contrib.auth.decorators import login_required
>>>>>>> origin

# Create your views here.
def home(request):
  return render(request,'home.html')

<<<<<<< HEAD
@login_required(login_url='/accounts/login/')
def profile(request,edit):
    current_user = request.user
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

def myProfile(request,id):
    user = User.objects.get(id = id)
    profiles = Profile.objects.get(user = user)
    
    return render(request,'profile.html',{"form":form,"profiles":profiles,"user":user})

=======
>>>>>>> origin
def post_request(request):    
    if request.method == 'POST':
        form = RequestForm(request.POST, request.FILES)
        if  form.is_valid():
            request = form.save(commit=False)
            request.save()
            name = request.business_name
            email = request.business_email
            send_notification_email(name, email)
            HttpResponseRedirect('home')
            return redirect('home')
  
    else:
        form =RequestForm()
<<<<<<< HEAD
    return render(request, 'register.html',{'form':form})    
=======
    return render(request, 'request_form.html',{'form':form})



@login_required(login_url='/accounts/login/')
def create_item(request,profile_id):
   current_user = request.user
   seller = Profile.objects.filter(id=profile_id.first)    
   if request.method == 'POST':
        form = ItemForm(request.POST, request.FILES)
        if form.is_valid():
            item = form.save(commit=False)
            items.profile = profile
            items.save()
        return redirect('view_profile')
   else:
        form = ItemForm()
   return render(request, 'create_items.html', {"form": form})
    
>>>>>>> origin
