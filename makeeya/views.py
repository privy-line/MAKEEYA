from django.shortcuts import render,redirect
from django.http  import HttpResponse,HttpResponseRedirect
from .forms import RequestForm
from django.contrib import messages
from .models import Buyer,Profile, Request, Category
from .email import send_notification_email
from django.contrib.auth.decorators import login_required

# Create your views here.
def home(request):
  return render(request,'home.html')

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
    