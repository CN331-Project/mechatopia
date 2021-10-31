from django.shortcuts import render

# Create your views here.
def home(request,user):
    a = user
    return render(request,'home.html',{'a':a})