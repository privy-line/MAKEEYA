from django.shortcuts import render
from django.http  import HttpResponse
from .forms import RequestForm
from django.contrib import messages
from .models import Buyer, Seller, Request, Category

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
            send_welcome_email(name, email)
            HttpResponseRedirect('home')
            return redirect('home')
  
    else:
        form =RequestForm()
    return render(request, 'request_form.html',{'form':form})