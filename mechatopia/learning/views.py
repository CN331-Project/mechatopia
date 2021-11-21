from django.shortcuts import redirect, render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth.models import User,auth
from task.models import Challenge,Challenge_test_case,Challenge_tag
from users.models import Progress,Pass,Code,Share_link
from users.models import User as User2
from learning.models import Lesson,Lesson_group,Assignment,Comment
import pandas as pd
import numpy as np
from datetime import datetime
#from .models import Course
#from users.models import Student

# Create your views here.



def learning(request):
	user_login_name = request.user 
	temp19 = User2.objects.all().filter(User_username = user_login_name,).values_list()
	s1=request.POST.get('s1', "");
	s2=request.POST.get('s2', "0");
	if s2 != "0" and s1 != "":
		temp2 = Lesson.objects.all().filter(Lesson_group_id = s2, Lesson_name__contains=s1)
	elif s2 != "0":
		temp2 = Lesson.objects.all().filter(Lesson_group_id = s2)
	elif s1 != "":
		temp2 = Lesson.objects.all().filter(Lesson_name__contains=s1)
	else:
		temp2 = Lesson.objects.all()
	temp3 = Lesson_group.objects.all()
	return render(request, "search_learning.html",{"temp2":temp2,"temp3":temp3,"a1":s2,"temp19":temp19})

def learning_bak(request):
	user_login_name = request.user 
	temp19 = User2.objects.all().filter(User_username = user_login_name,).values_list()
	return render(request, "search_learning_bak.html")

    
def articles(request,learning_id):
	user_login_name = request.user 
	temp19 = User2.objects.all().filter(User_username = user_login_name,).values_list()
	user_login_name = request.user 
	temp6 = User.objects.all().filter(username = user_login_name).values_list()
	temp7 = temp6[0]
	temp2 = Lesson.objects.all().filter(Lesson_ID = learning_id).values_list()
	temp3 = temp2[0]
	lg_id = temp3[8]
	re1 = []
	count = 0
	count2 = 0
	as_result = []
	re_url = 0
	temp4 = Lesson.objects.all().filter(Lesson_group_id = lg_id).values_list()
	if temp4.exists():
		for j in temp4:
			if j[0] != temp3[0]:
				re1.append(j)
				count+=1
			else:
				count2 = count
	re1 = re1[count2-2:count2+2]
	temp = Lesson_group.objects.all().filter(Lesson_group_ID = temp3[8])
	group = temp[0].Lesson_group_name
	temp = User.objects.all().filter(id = temp3[7])
	admin = temp[0].username
	complete = []
	score_list = []
	y = []
	score = "a / b"
	temp5 = Assignment.objects.all().filter(Assignment_lesson_id = learning_id).values_list()
	for i in temp5:
		url = i[3]
		url2 = 'https://docs.google.com/spreadsheets/d/' + url.split('/')[-2] + "/export?format=csv"
		re_url = url2
		test = pd.read_csv(url2)
		test2 = test.to_numpy()
#		x = test.head()  
#		null_df = pd.DataFrame([],[])
#		b = x[x['username'] == "andy"]
		for k in range(1,len(test2)+1):
			if test2[-1*k][2] == str(user_login_name):
				y.append(test2[-1*k])
				break;
		if len(y) != 0:
			tt = 0
			t = 0 
			for j in y[-1]:
				if "/" in str(j):
					t = tt
				tt+=1
			score = y[-1][t]	
			score_list.append(score)	
		else:
			score_list.append("0 / 0")
		temp8 = Progress.objects.all().filter(Progress_user_id = temp7[0],Progress_assignment_id = i[0]).values_list()
		if score.split(" / ")[0] == score.split(" / ")[1]:			
			if len(temp8)==0:
				adder = Progress(
					Progress_user_id = temp7[0],
					Progress_assignment_id = i[0],
					Progress_lesson_id = learning_id,
			        )                
				adder.save()
		if len(temp8)!=0:
			complete.append(1)
		else:
			complete.append(0)
	###### comment
	temp8 = Comment.objects.all().filter(Comment_object_id = learning_id, Comment_object_is = 1).values_list()
	temp8 = list(temp8)
	for m in range(len(temp8)):		
		temp9 = User2.objects.all().filter(idd = temp8[m][2]).values_list()
		temp8[m]=list(temp8[m])
		temp8[m].append(temp9[0][1])
		temp8[m].append(temp9[0][7])
	return render(request, "learning_article.html",{"df":temp8,'score':score,"temp3":temp3,"re1":re1,"group":group
		,"admin":admin,"temp5":temp5,"as_result":as_result,"re_url":re_url,"complete":complete,"score_list":score_list
		,"user_id":temp7[0],"comment_list":temp8,"temp19":temp19})

# return  HttpResponseRedirect(reverse('urlname')) c.loc[c.username[1]][2]
def comment(request,object_id,object_is):
	a1=request.POST.get('user_id', '');
	a2=request.POST.get('comment_text', 0);
	now = datetime.now()
	a4=date_time = now.strftime("%Y/%m/%d")
	adder = Comment(
					Comment_user_id = a1,
					Comment_text = a2,
					Comment_object_id = object_id,
					Comment_object_is = object_is,
					Comment_date = a4,
			        )                
	adder.save()
	if object_is == 1: #lesson
		return redirect(reverse('articles',args =(object_id,)))

#	elif object_is == 2: #challenge
#		return redirect(reverse('admin_add_tag',args =(have_message,)))

	elif object_is == 3: #lab
		return redirect(reverse('workspace',args =(object_id,)))


		

