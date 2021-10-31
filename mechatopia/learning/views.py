from django.shortcuts import render

# Create your views here.
def home(request,user_firstname):
    return render(request,'home.html')