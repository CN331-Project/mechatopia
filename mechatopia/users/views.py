from django.shortcuts import render,redirect
from django.contrib.auth import authenticate
from django.contrib import auth

# Create your views here.


def welcome(request):
    return render(request,'index.html')

def loginform(request):
    username = request.POST['Username']
    password = request.POST['Password']

    user = authenticate(username=username, password=password)
    if user is not None :
        auth.login(request,user)
        return redirect('home',{'user':user})
    else:
        return redirect('/')
def logout(request):
    auth.logout(request)
    return redirect("/")