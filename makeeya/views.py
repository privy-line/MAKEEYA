from django.shortcuts import render,redirect
from django.http  import HttpResponse
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .models import Profile,Request,Buyer,Item
from .forms import ProfileForm,RequestForm,ItemForm
from .email import send_notification_email
import datetime

# Create your views here.
def home(request):
  return render(request,'home.html')

# @login_required(login_url='/accounts/login/')
def profile(request,edit):
    current_user = request.user
    profile=Profile.objects.get(user=current_user)
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            profile.business_name=form.data
            profile.business_description=form.data
            profile.business_logo = form.cleaned_data['business_logo']
            profile.business_email = form.cleaned_data['business_email']
            profile.business_address = form.cleaned_data['business_address']
            profile.user=current_user
            
            profile.save()
            return redirect('home')
    else:
        form = ProfileForm()
    return render(request, 'profile_form.html', {"form": form,'user':current_user,"profile":profile})

def myProfile(request,id):
    user = User.objects.get(id = id)
    profile = Profile.objects.filter(user = user).first()
    
    return render(request,'profile.html',{"profile":profile,"user":user})

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
        form = RequestForm()
    return render(request, 'register.html',{'form':form})    

@login_required(login_url='/accounts/login/')
def create_item(request,id):
    current_user = request.user
    profile = Profile.objects.filter(id=id).first()    
    if request.method == 'POST':
        form = ItemForm(request.POST, request.FILES)
        if form.is_valid():
            item = form.save(commit=False)
            items.profile = profile
            items.save()
        return redirect('myProfile')
    else:
        form = ItemForm()
    return render(request, 'create_item.html', {"form": form,"profile":profile})

def last_day(request):
    today = datetime.date.today()
    last_day_items = Item.objects.filter(expiry_date=today)
    return render(request,'home.html',{"last_day_items":last_day_items})
    
