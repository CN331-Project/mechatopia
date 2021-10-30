from django.shortcuts import redirect, render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.models import User,auth
#from .models import Course
#from users.models import Student

# Create your views here.


def welcome(request):
    return render(request,'about.html')


def dashboard(request):
    return render(request, "dashboard.html")
    

def tem(request):
    return render(request, "tem.html")



# return  HttpResponseRedirect(reverse('urlname'))





