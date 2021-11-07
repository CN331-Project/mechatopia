from django.shortcuts import render

# Create your views here.
from task.models import Lab

def lab(request):
   return render(request,'lab.html')

def challenge(request):
   return render(request,'challenge.html')

def challengeX(request):
   return render(request,'chalengeX.html')