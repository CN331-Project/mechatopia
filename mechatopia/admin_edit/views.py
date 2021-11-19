from django.shortcuts import redirect, render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.models import User,auth
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate
from django.contrib import auth
from django.contrib import messages
from task.models import Challenge,Challenge_test_case,Challenge_tag
from task.models import Lab_tag,Lab,Lab_in_tag,Challenge_in_tag
from learning.models import Lesson_group,Lesson,Assignment
from users.models import User as User2
from users.models import Progress,Code,Pass
from django.core.files.storage import FileSystemStorage
import os
from shutil import copyfile
from datetime import datetime


def admin_dashboard(request):
	return render(request, "admin_dashboard.html")


def admin_add_tag(request,have_message):
	return render(request, "admin_add_tag.html",{"have_message":have_message})


def admin_add_tag_p(request):
	have_message = 0
	a1=request.POST.get('a1', '');
	if a1 == "1":
		tag_name=request.POST.get('tag_name', '');
		if Challenge_tag.objects.filter(Challenge_tag_name=tag_name).exists():
			messages.info(request,'Challenge tag name exists')
			have_message = 2

		else:
			adder = Challenge_tag(Challenge_tag_name = tag_name, 
	        )                
			adder.save() 
			messages.info(request,'add Challenge tag success' )
			have_message = 1
	else:
		tag_name=request.POST.get('tag_name', '');
		if Lab_tag.objects.filter(Lab_name=tag_name).exists():
			messages.info(request,'Lab tag name exists')
			have_message = 2
		else:
			adder = Lab_tag(Lab_name = tag_name,
			)
			adder.save() 
			messages.info(request,'add Lab tag success' )
			have_message = 1
	return redirect(reverse('admin_add_tag',args =(have_message,)))


def admin_add_lesson_group(request,have_message):
	return render(request, "admin_add_lesson_group.html",{"have_message":have_message})


def admin_add_lesson_group_p(request):
	have_message = 0
	a1=request.POST.get('group_name', '');
	a2=request.POST.get('description', '');
	a3=request.POST.get('pic', '');
	now = datetime.now()
	a4=date_time = now.strftime("%Y/%m/%d")
	pic_name = "default.jpg"

	user_login_name = request.user 
	temp2 = User.objects.all().filter(username = user_login_name).values_list()
	a5 = temp2[0][0]
	temp5 = Lesson_group.objects.all().order_by('-Lesson_group_ID').values_list()
	if temp5.exists():
		a11 = temp5[0][0]
	else:
		a11 = 0

	if Lesson_group.objects.filter(Lesson_group_name=a1).exists():
		messages.info(request,'Lesson group name exist' )
		have_message = 2	
	else:		
		pic_path = "temp_pic/"
		if request.method == 'POST' and request.FILES['pic']:
			mypic = request.FILES['pic']
			fs = FileSystemStorage()
			name = "lgpic_" + str(a11) + ".jpg"

			if os.path.isfile("file/" + pic_path + name):
				os.remove("file/" + pic_path + name)

			filename = fs.save(pic_path + name , mypic)
			uploaded_file_url = fs.url(filename)
			pic_name = name

			copyfile("file/" + pic_path + name, "static/lesson/lgpic/" + name)
			os.remove("file/" + pic_path + name)					
		adder = Lesson_group(
			Lesson_group_name = a1,
			Lesson_group_description = a2,
			Lesson_group_admin_add = a5,
			Lesson_group_recent_date = a4,
			Lesson_group_pic = pic_name,
	        )                
		adder.save() 
		messages.info(request,'add Lesson Group success' )
		have_message = 1
	return redirect(reverse('admin_add_lesson_group',args =(have_message,)))


def admin_add_lesson(request,have_message):
	temp2 = Lesson_group.objects.all()
	return render(request, "admin_add_lesson.html",{"have_message":have_message,"temp2":temp2,})

def admin_add_lesson_p(request):
	have_message = 0
	a1=request.POST.get('lesson_name', '');
	a2=request.POST.get('description', '');
	a5=request.POST.get('group_id', '');
	a6=request.POST.get('link', '');
	now = datetime.now()
	a4=date_time = now.strftime("%Y/%m/%d")
	pic_name = "default.jpg"
	pic_name2 = "default.jpg"
	user_login_name = request.user 
	temp2 = User.objects.all().filter(username = user_login_name).values_list()
	a7 = temp2[0][0]
	temp5 = Lesson.objects.all().order_by('-Lesson_ID').values_list()
	if temp5.exists():
		a11 = temp5[0][0]
	else:
		a11 = 0

	if Lesson.objects.filter(Lesson_name=a1).exists():
		messages.info(request,'Lesson name exist' )
		have_message = 2	
	else:		
		pic_path = "temp_pic/"
		if request.method == 'POST' and request.FILES['pic']:
			mypic = request.FILES['pic']
			fs = FileSystemStorage()
			name = "lesson_pic_" + str(a11) + ".jpg"

			if os.path.isfile("file/" + pic_path + name):
				os.remove("file/" + pic_path + name)

			filename = fs.save(pic_path + name , mypic)
			uploaded_file_url = fs.url(filename)
			pic_name = name

			copyfile("file/" + pic_path + name, "static/lesson/lesson_pic/" + name)
			os.remove("file/" + pic_path + name)
		if request.method == 'POST' and request.FILES['cover_pic']:
			mypic2 = request.FILES['cover_pic']
			fs2 = FileSystemStorage()
			name2 = "lesson_cover_pic_" + str(a11) + ".jpg"

			if os.path.isfile("file/" + pic_path + name2):
				os.remove("file/" + pic_path + name2)

			filename2 = fs2.save(pic_path + name2 , mypic2)
			uploaded_file_url = fs2.url(filename2)
			pic_name2 = name2

			copyfile("file/" + pic_path + name2, "static/lesson/lesson_cover_pic/" + name2)
			os.remove("file/" + pic_path + name2)
		adder = Lesson(
			Lesson_name = a1,
			Lesson_description = a2,
			Lesson_link = a5,
			Lesson_date = a4,
			Lesson_admin_add = a7,
			Lesson_group_id = a5,
			Lesson_pic = pic_name,
			Lesson_cover_pic = pic_name2,
	        )                
		adder.save() 
		messages.info(request,'add Lesson success' )
		have_message = 1
	return redirect(reverse('admin_add_lesson',args =(have_message,)))

def admin_add_lab(request,have_message):
	temp2 = Lab_tag.objects.all()
	return render(request, "admin_add_lab.html",{"have_message":have_message,"temp2":temp2,})

def admin_add_lab_p(request):
	have_message = 0
	a1=request.POST.get('lab_name', '');
	a2=request.POST.get('lab_link', '');
	a3=request.POST.getlist('lab_tag_id[]', '');
	a4=request.POST.get('lab_des', '');
	pic_name = "default.jpg"
	temp5 = Lab.objects.all().order_by('-Lab_ID').values_list()
	if temp5.exists():
		a11 = temp5[0][0]
	else:
		a11 = 0
	if Lab.objects.filter(Lab_name=a1).exists():
		messages.info(request,'Lab name exist' )
		have_message = 2	
	else:		
		pic_path = "temp_pic/"
		if request.method == 'POST' and request.FILES['pic']:
			mypic = request.FILES['pic']
			fs = FileSystemStorage()
			name = "lab_pic_" + str(a11) + ".jpg"

			if os.path.isfile("file/" + pic_path + name):
				os.remove("file/" + pic_path + name)

			filename = fs.save(pic_path + name , mypic)
			uploaded_file_url = fs.url(filename)
			pic_name = name

			copyfile("file/" + pic_path + name, "static/lab/lab_pic/" + name)
			os.remove("file/" + pic_path + name)
		if request.method == 'POST' and request.FILES['cover_pic']:
			mypic2 = request.FILES['cover_pic']
			fs2 = FileSystemStorage()
			name2 = "lab_cover_pic_" + str(a11) + ".jpg"

			if os.path.isfile("file/" + pic_path + name2):
				os.remove("file/" + pic_path + name2)

			filename2 = fs2.save(pic_path + name2 , mypic2)
			uploaded_file_url = fs2.url(filename2)
			pic_name2 = name2

			copyfile("file/" + pic_path + name2, "static/lab/lab_cover_pic/" + name2)
			os.remove("file/" + pic_path + name2)
		adder = Lab(
			Lab_name = a1,
			Lab_link = a2,			
			Lab_pic = pic_name,
			Lab_cover_pic = pic_name2,
			Lab_description = a4,
	        )                
		adder.save() 
		temp3 = Lab.objects.all().filter(Lab_name = a1).values_list()
		a7 = temp3[0][0]
		for i in a3:
			adder2 = Lab_in_tag(
			Lab_tag_id = i,
			Lab_id = a7,
	        )                
			adder2.save()
		messages.info(request,'add Lab success' )
		have_message = 1
	return redirect(reverse('admin_add_lab',args =(have_message,)))

def admin_add_challenge(request,have_message):
	temp2 = Challenge_tag.objects.all()
	return render(request, "admin_add_challenge.html",{"have_message":have_message,"temp2":temp2,})

def admin_add_challenge_p(request):
	have_message = 0
	a1=request.POST.get('challenge_name', '');
	a2=request.POST.get('description', '');
	a3=request.POST.get('level', '');	
	a4=0	
	a6=request.POST.getlist('challenge_tag_id[]', '');
	pic_name = "default.jpg"
	now = datetime.now()
	a5=date_time = now.strftime("%Y/%m/%d")
	temp5 = Challenge.objects.all().order_by('-Challenge_ID').values_list()
	if temp5.exists():
		a11 = temp5[0][0]
	else:
		a11 = 0
	if Challenge.objects.filter(Challenge_question=a1).exists():
		messages.info(request,'Lab name exist' )
		have_message = 2	
	else:		
		pic_path = "temp_pic/"
		if request.method == 'POST' and request.FILES['pic']:
			mypic = request.FILES['pic']
			fs = FileSystemStorage()
			name = "challenge_pic_" + str(a11) + ".jpg"

			if os.path.isfile("file/" + pic_path + name):
				os.remove("file/" + pic_path + name)

			filename = fs.save(pic_path + name , mypic)
			uploaded_file_url = fs.url(filename)
			pic_name = name

			copyfile("file/" + pic_path + name, "static/challenge/challenge_pic/" + name)
			os.remove("file/" + pic_path + name)
		adder = Challenge(
			Challenge_question = a1,
			Challenge_description = a2,			
			Challenge_date = a5,
			Challenge_score = a4,
			Challenge_level = a3,
			Challenge_file = pic_name,
	        )                
		adder.save() 
		temp3 = Challenge.objects.all().filter(Challenge_question = a1).values_list()
		a7 = temp3[0][0]
		for i in a6:
			adder2 = Challenge_in_tag(
			Challenge_tag_id = i,
			Challenge_id = a7,
	        )                
			adder2.save()
		messages.info(request,'add Challenge success' )
		have_message = 1
	return redirect(reverse('admin_add_challenge',args =(have_message,)))

def admin_add_testcase(request,have_message):
	temp2 = Challenge.objects.all()
	return render(request, "admin_add_testcase.html",{"have_message":have_message,"temp2":temp2,})

def admin_add_testcase_p(request):	
	ch_id = request.POST.get('ch_id', '');
	return render(request, "admin_add_testcase_p.html",{"ch_id":ch_id})

def admin_add_testcase_pp(request):
	have_message = 0
	ch_id=request.POST.get('ch_id', '');
	score1=int(request.POST.get('score1', '0'));
	score2=int(request.POST.get('score2', '0'));
	score3=int(request.POST.get('score3', '0'));
	score4=int(request.POST.get('score4', '0'));
	score5=int(request.POST.get('score5', '0'));
	code_st_path = "temp_code/"	
	list_score = [score1 , score2 , score3 , score4 , score5]
	score = score1 + score2 + score3 + score4 + score5
	for i in range(1,6):
		if list_score[i-1]!=0:
			if request.method == 'POST' and request.FILES["test"+str(i)]:
				myfile = request.FILES["test"+str(i)]
				fs = FileSystemStorage()
				name = "test_" + "ch_" + str(ch_id) + "_cht" + str(i) + ".txt"
				test_name = name

				if os.path.isfile("file/" + code_st_path + name):
					os.remove("file/" + code_st_path + name)  

				filename = fs.save(code_st_path + name , myfile)
				uploaded_file_url = fs.url(filename)
				copyfile("file/" + code_st_path + name, "static/challenge/challenge_test/" + name)
				os.remove("file/" + code_st_path + name)

				myfile = request.FILES["ans"+str(i)]
				fs = FileSystemStorage() 
				name = "ans_" + "ch_" + str(ch_id) + "_cht" + str(i) + ".txt"
				ans_name = name

				if os.path.isfile("file/" + code_st_path + name ):
					os.remove("file/" + code_st_path + name )  

				filename = fs.save(code_st_path + name , myfile)
				uploaded_file_url = fs.url(filename)
				copyfile("file/" + code_st_path + name, "static/challenge/challenge_answer/" + name)
				os.remove("file/" + code_st_path + name)

				adder = Challenge_test_case(
				Challenge_test_challenge_id = ch_id,
				Challenge_test_no = i,			
				Challenge_test_score = list_score[i-1],
				Challenge_test_test = test_name,
				Challenge_test_answer = ans_name,
		        )                
				adder.save() 

			else:
				have_message = 0
	scoreupdate = Challenge.objects.get(Challenge_ID=ch_id)
	scoreupdate.Challenge_score = score
	scoreupdate.save() 
	messages.info(request,'add Challenge testcase success' )
	have_message = 1
	return redirect(reverse('admin_add_testcase',args =(have_message,)))

def admin_add_assignment(request,have_message):
	temp2 = Lesson.objects.all()
	return render(request, "admin_add_ass.html",{"have_message":have_message,"temp2":temp2,})

def admin_add_assignment_p(request):	
	ls_id = request.POST.get('ls_id', '');
	return render(request, "admin_add_ass_p.html",{"ls_id":ls_id})	

def admin_add_assignment_pp(request):	
	have_message = 0
	no = 1
	ls_id = request.POST.get('ls_id', '');
	add1=request.POST.get('add1', '');
	add2=request.POST.get('add2', '');
	add3=request.POST.get('add3', '');
	if add1 == "1":
		flink = request.POST.get('flink1', '');
		slink = request.POST.get('slink1', '');
		dele = Assignment.objects.filter(Assignment_lesson_id=ls_id,Assignment_no=1)
		dele.delete()
		adder = Assignment(
			Assignment_lesson_id = ls_id,
			Assignment_test = flink,			
			Assignment_answer = slink,
			Assignment_no = no,
	        )                
		adder.save() 
		no+=1
		have_message = 1
	if add2 == "1":
		flink = request.POST.get('flink2', '');
		slink = request.POST.get('slink2', '');
		dele = Assignment.objects.filter(Assignment_lesson_id=ls_id,Assignment_no=2)
		dele.delete()
		adder = Assignment(
			Assignment_lesson_id = ls_id,
			Assignment_test = flink,			
			Assignment_answer = slink,
			Assignment_no = no,
	        )                
		adder.save() 
		no+=1
		have_message = 1
	if add3 == "1":
		flink = request.POST.get('flink3', '');
		slink = request.POST.get('slink3', '');
		dele = Assignment.objects.filter(Assignment_lesson_id=ls_id,Assignment_no=3)
		dele.delete()
		adder = Assignment(
			Assignment_lesson_id = ls_id,
			Assignment_test = flink,			
			Assignment_answer = slink,
			Assignment_no = no,
	        )                
		adder.save() 
		no+=1
		have_message = 1
	messages.info(request,'add Lesson Assignment success' )
	return redirect(reverse('admin_add_assignment',args =(have_message,)))