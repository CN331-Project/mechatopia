from django.shortcuts import redirect, render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.models import User,auth
#from .models import Course
#from users.models import Student

# Create your views here.


def challenge(request):
    return render(request, "dashboard.html")
    

def lab(request):
    return render(request, "tem.html")



# return  HttpResponseRedirect(reverse('urlname'))





