from django.shortcuts import render,redirect
from django.contrib.auth import authenticate
from django.contrib import auth
from django.contrib.auth.models import User
from django.contrib import messages
from .models import Proflie
# Create your views here.


def welcome(request):
    return render(request,'index.html')

def loginform(request):
    username = request.POST['Username']
    password = request.POST['Password']

    user = authenticate(username=username, password=password)
    if user is not None :
        auth.login(request,user)
        return redirect('home')
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

    if password == repassword:
        if User.objects.filter(username=username).exists():
            messages.info(request,'ผู้ใช้นี้ถูกใช้แล้ว')
            return redirect('signup')
        elif User.objects.filter(email=email).exists():
            messages.info(request,'email นี้ลงทะเบียนแล้ว')
            return redirect('signup')
        else:
            add_user = User.objects.create_user(
            username = username,
            password = password,
            email = email,
            first_name = firstname,
            last_name = secondname
            )
            add_user.save()
            return render(request,'index.html')
    else:
            messages.info(request,'กรอกรหัสผ่านไม่ตรงกัน')
            return redirect('signup')

def setting(request):
    data = Proflie.objects.filter(user = request.user.id)
    return render(request, "setting.html",{'data':data})

def editprofile(request):
    faculty = request.POST['faculty']
    major = request.POST['major']
    if faculty == '':
        return redirect('setting')
    else:
        edit = Proflie.objects.get(user = request.user.id)
        edit.faculty = faculty
        edit.save()
        edit_major = Proflie.objects.get(user = request.user.id)
        edit_major.major = major
        edit_major.save()
        return redirect('setting')

def logout(request):
    auth.logout(request)
    return redirect("/")