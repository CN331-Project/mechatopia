from django.shortcuts import redirect, render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.models import User,auth
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate
from django.contrib import auth
from django.contrib import messages
from task.models import Challenge,Challenge_test_case,Challenge_tag
from users.models import User as User2
from users.models import Progress,Code,Pass
from django.core.files.storage import FileSystemStorage
import os
#from .models import Course
#from users.models import Student

# Create your views here.

def welcome(request):
    return render(request,'index.html') # เอาออก


def tem(request):
    return render(request, "tem.html")


####################### ไม่ใช้ #######################################

def dashboard(request):
    #temp2 = User.objects.all().filter(email = "sss@sss.com").values_list()
    user_login_name = request.user 
    temp2 = User.objects.all().filter(username = user_login_name).values_list()
    temp3 = User2.objects.all().filter(User_username = user_login_name).values_list()
    is_admin = temp3[0][4]
    return render(request, "dashboard.html",{"temp2":temp2,"temp3":temp3,"is_admin":is_admin})


def login(request):
    return render(request, "login.html")



def check_login(request):
    email = request.POST['email']
    password = request.POST['password']
    temp2 = User.objects.all().filter(email = email).values_list()
    username = temp2[0][4]

    user = authenticate(username=username, password=password)
    if user is not None :
        auth.login(request,user)
        return redirect('/dashboard')
    else:
        messages.info(request,'try again' )
        return redirect('/login')

def signup(request):
    return render(request,'signup.html')

def signupform(request):
    username = request.POST['Username']
    #firstname = request.POST['Firstname']
    #secondname = request.POST['Secondname']
    email = request.POST['Email']
    password = request.POST['Password']
    repassword = request.POST['Re-Password']
    bio = request.POST['bio']
    pic_name = "default.jpg"

    if password == repassword:
        if User.objects.filter(username=username).exists():
            messages.info(request,'ผู้ใช้นี้ถูกใช้แล้ว')
            return redirect('/signup')
        if password == "" or email == "" or repassword == "":
            messages.info(request,'โปรดกรอกข้อมูลให้ครบ')
            return redirect('/signup')
        elif User.objects.filter(email=email).exists():
            messages.info(request,'email นี้ลงทะเบียนแล้ว')
            return redirect('/signup')
        else:
            upic_path = "user_pic/"
            if request.method == 'POST' and request.FILES['pic']:
                mypic = request.FILES['pic']
                fs = FileSystemStorage()
                name = "upic_" + username + ".jpg"

                if os.path.isfile("file/" + upic_path + name):
                    os.remove("file/" + upic_path + name)

                filename = fs.save(upic_path + name , mypic)
                uploaded_file_url = fs.url(filename)
                pic_name = name

            add_user = User.objects.create_user(
            username = username,
            password = password,
            email = email,
            #first_name = firstname,
            #last_name = secondname            
            )
            add_user.save()

            adder_user = User2(User_username=username,
            User_email = email,
            User_is_admin=False,
            User_score=0,
            User_rank="Bronze",
            User_pic= name,
            User_bio=bio, 
            )                
            adder_user.save()  
    
            





            return redirect('/login')
    else:
        messages.info(request,'รหัสผ่านไม่ตรงกัน')
        return redirect('/signup')



    

def logout(request):
    auth.logout(request)
    return redirect("/login")


# return  HttpResponseRedirect(reverse('urlname'))


"""
adder = Register(User_ID=a1,
                SID=a2,
                Status=1,
                Date=datetime.datetime.now(),
                Grade = 0
                )                
                adder.save()        
                messages.info(request,'ลงทะเบียนสำเร็จ')
                subupdate = Subject.objects.get(SID=a2)
                subupdate.Sitting = subupdate.Sitting+1
                subupdate.save() 
                """


