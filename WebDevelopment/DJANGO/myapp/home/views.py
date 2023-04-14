import imp
from multiprocessing import context
from datetime import datetime
import re
from django.shortcuts import render
from home.models import Contact
from django.contrib import messages
# Create your views here.
from django.http import HttpResponse

from home.models import Contact

def index(request):
   # return HttpResponse("home")
   return render(request, 'index.html')


def about(request):
   return render(request, 'about.html')

def services(request):
   return render(request, 'services.html')

def contact(request):
   if request.method =="POST":
      name = request.POST.get('name')
      email = request.POST.get('email')
      desc = request.POST.get('desc')
      contact = Contact(name=name, email=email, desc=desc, date=datetime.today())
      contact.save()
      messages.success(request, 'your massage has been sent')
   return render(request, 'contact.html')