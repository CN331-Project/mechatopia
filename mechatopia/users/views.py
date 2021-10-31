from django.shortcuts import render,redirect
from django.contrib.auth import authenticate
from django.contrib import auth
from django.contrib.auth.models import User

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

def signup(request):
    return render(request,'signup.html')

def account(request):
    username = request.POST['Username']
    firstname = request.POST['Firstname']
    secondname = request.POST['Secondname']
    email = request.POST['Email']
    password = request.POST['Password']
    repassword = request.POST['Re-Password']

    add_user = User.objects.create_user(
        username = username,
        password = password,
        email = email,
        first_name = firstname,
        last_name = secondname
    )

    add_user.save()

    return render(request,'index.html')

def logout(request):
    auth.logout(request)
    return redirect("/")