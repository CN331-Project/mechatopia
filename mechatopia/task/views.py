from django.shortcuts import redirect, render
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.models import User,auth
from users.models import Progress,Code,Pass,Share_link
from users.models import User as User2
from learning.models import Lesson,Lesson_group,Assignment,Comment
from task.models import Challenge,Challenge_test_case,Challenge_tag
from task.models import Lab_tag,Lab,Lab_in_tag,Challenge_in_tag
from django import forms
from django.core.files.storage import FileSystemStorage
import os
from django.conf import settings
from subprocess import Popen, PIPE
import subprocess
# Create your views here.


def challenge(request):
	a1=''   #text
	a2=0	#level
	a3=0	#tag
	a1=request.POST.get('a1', '');
	a2=request.POST.get('a2', 0);
	a3=request.POST.get('a3', 0);
	all_tag = Challenge_tag.objects.all()
#    if(a1 != ''):
	temp = Challenge.objects.all().filter()
	return render(request, "search_challenge.html",{"all_tag":all_tag,"temp":temp,"a1":a1,"a2":a2,"a3":a3})


def simple_upload(request,challenge_id):
	code_st_path = "challenge_code/"
	user_login_name = request.user 
	temp9 = User2.objects.all().filter(User_username = user_login_name,).values_list()
	user_id = temp9[0][9]
	if request.method == 'POST' and request.FILES['mycode']:
		myfile = request.FILES['mycode']
		fs = FileSystemStorage()
		name = "code_" + str(user_id) + "_" + str(challenge_id)

		if os.path.isfile("file/" + code_st_path + name + ".txt"):
			os.remove("file/" + code_st_path + name + ".txt")  

		filename = fs.save(code_st_path + name + ".txt" , myfile)
		uploaded_file_url = fs.url(filename)
		adder = Code(
				Code_filename = name + ".txt",
				Code_user_id = user_id,
				Code_challenge_id = challenge_id,
			)                
		adder.save()
		return redirect(reverse('problem',args=(challenge_id,)))
	else:
		return redirect(reverse('problem',args=(challenge_id,)))

def simple_upcode(request,challenge_id):
	code_st_path = "challenge_code/"
	code_box = request.POST.get('code_box', False);
	user_login_name = request.user 
	temp9 = User2.objects.all().filter(User_username = user_login_name,).values_list()
	user_id = temp9[0][9]
	if request.method == 'POST':
		name = "code_" + str(user_id) + "_" + str(challenge_id)
		code_file = "file/" + code_st_path + name + ".txt"
		if os.path.isfile(code_file):
			os.remove(code_file)  

		file1 = open(code_file,"w")
		file1.write("".join(code_box.split("\n")))
	#	file1.writelines(lines3)
		file1.close()
		adder = Code(
				Code_filename = name + ".txt",
				Code_user_id = user_id,
				Code_challenge_id = challenge_id,
			)                
		adder.save()
		return redirect(reverse('problem',args=(challenge_id,)))	
	return redirect(reverse('problem',args=(challenge_id,)))

def problem(request,challenge_id):
	user_login_name = request.user 
	temp9 = User2.objects.all().filter(User_username = user_login_name,).values_list()
	user_id = temp9[0][9]
	user_score = temp9[0][5]
	have_code = 0
	code_temp = ""
	link = ""
	temp = Challenge.objects.all().filter(Challenge_ID = challenge_id).values_list()
	temp2 = Challenge_test_case.objects.all().filter(Challenge_test_challenge_id = challenge_id).values_list()
	temp3 = Code.objects.all().filter(Code_challenge_id = challenge_id,Code_user_id = user_id).values_list()
	if temp3.exists():
		have_code=1
	path_test = "static/challenge/challenge_test/"
	path_answer = "static/challenge/challenge_answer/"
	path_py = "file/challenge_code/temp_py/"
	path_code = "file/challenge_code/"
	file_test = open(os.path.join(settings.BASE_DIR, path_test + temp2[0][4]))
	file_answer = open(os.path.join(settings.BASE_DIR, path_answer + temp2[0][5]))
	if have_code==1:
		code_temp = temp3[0][1]
	else:
		code_temp = "null.txt"
	file_code = os.path.join(settings.BASE_DIR, path_code + code_temp)
	score = 0
	correct = 0
	count = 0
	output = ""
	lines4 = ""

	for i in temp2:
		count+=1
		with open(os.path.join(settings.BASE_DIR, path_test + i[4])) as f:
			lines1 = f.read()

		with open(os.path.join(settings.BASE_DIR, path_answer + i[5])) as f:
			lines2 = f.read()


		if os.path.isfile(file_code):
			with open(os.path.join(file_code)) as f:
				lines4 = f.read()

			lines3 = []
			with open(os.path.join(file_code)) as f:
				lines3 = f.readlines()
			for j in range(len(lines3)):
				lines3[j] = lines3[j].replace("input()","sys.argv[" + "next(counter)" + "]")

			temp_py_file = os.path.join(settings.BASE_DIR, path_py + "code_"+ str(user_id) +"_" + str(challenge_id) +".py")
			file1 = open(temp_py_file,"w")
			file1.write("from itertools import count \n")
			file1.write("import sys \n")
			file1.write("counter = count(1) \n")
			#file1.write("print(sys.argv[1]) \n")
			file1.writelines(lines3)
			file1.close()

			run = "python " + temp_py_file + " " + " ".join(lines1.split("\n")) + " \n "
			
			p = subprocess.Popen(run, stdout=subprocess.PIPE)
			output = p.communicate()[0].decode()
			if lines2.split() == output.split():
				correct+=1
				score+=i[3]

	temp4 = Pass.objects.all().filter(Pass_challenge_id = challenge_id,Pass_user_id = user_id).values_list()
	if temp4.exists():
		a=5
	else:
		if count == correct:
			adder = Pass(
			Pass_challenge_id = challenge_id,
			Pass_user_id = user_id,
	        )
			adder.save()
			scoreupdate = User2.objects.get(idd=int(user_id))
			scoreupdate.User_score = user_score + score 
			scoreupdate.save() 

	return render(request, "problem.html",{'link':link,'query':temp,'user_id':user_id,'challenge_id':challenge_id,
				'temp2':lines1.split("\n"),'temp3':output.split(),'temp4':lines2.split(),"score":score,"code_box":lines4,
				"score":score,"count":count,"correct":correct,"tag":user_id})     
      

def lab(request):
	s1=request.POST.get('s1', "");
	s2=request.POST.get('s2', "0");
	a = 0
	temp5 = []
#	if s2 != "0" and s1 != "":
#		temp2 = Lab_in_tag.objects.all().filter(Lab_tag_id = s2)
	if s1 != "":
		temp2 = Lab.objects.all().filter(Lab_name__contains=s1).values_list()
	elif s2 != "0":		
		temp2 = Lab_in_tag.objects.all().filter(Lab_tag_id = int(s2)).values_list()
		temp2 = list(temp2)
		for i in range(len(temp2)):
			temp4 = Lab.objects.all().filter(Lab_ID=temp2[i][1]).values_list()
			temp5.append(temp4[0])
			a = 3
		temp2 = temp5[:]	
	else:
		temp2 = Lab.objects.all().values_list()
	temp3 = Lab_tag.objects.all()
	return render(request, "search_lab.html",{"temp2":temp2,"temp3":temp3,"a1":temp2})


def workspace(request,lab_id):
	user_login_name = request.user 
	tag = []
	temp2 = Lab.objects.all().filter(Lab_ID = lab_id).values_list()
	temp3 = temp2[0]
	temp4 = Lab_in_tag.objects.all().filter(Lab_id = lab_id).values_list()
	fst_re = temp4[0][2]
	for i in temp4:
		temp5 = Lab_tag.objects.all().filter(Lab_tag_ID = i[2]).values_list()
		for j in temp5:
			tag.append(j[1])
	tag = ", ".join(tag)
	re1 = []
	count=0
	count2=0
	temp6 = Lab_in_tag.objects.all().filter(Lab_tag_id = fst_re).values_list()
	if temp6.exists():
		for k in temp6:
			if k[1] != lab_id:
				temp7 = Lab.objects.all().filter(Lab_ID = k[1]).values_list()
				for l in temp7:
					re1.append(l)
					count+=1
			else:
				count2 = count
	re1 = re1[count2-3:count2+3]
	link = ""
	temp9 = User2.objects.all().filter(User_username = user_login_name,).values_list()
	user_id = temp9[0][9]
	temp10 = Share_link.objects.all().filter(Share_user_id = user_id,Share_lab_id = lab_id).values_list()
	if temp10.exists():
		link = temp10[0][3]
	else:
		link = temp3[2]
	###### comment
	temp8 = Comment.objects.all().filter(Comment_object_id = lab_id, Comment_object_is = 3).values_list()
	temp8 = list(temp8)
	for m in range(len(temp8)):		
		temp9 = User2.objects.all().filter(idd = temp8[m][2]).values_list()
		temp8[m]=list(temp8[m])
		temp8[m].append(temp9[0][1])
		temp8[m].append(temp9[0][7])

	return render(request, "workspace.html",{"temp3":temp3,"tag":tag,"re1":re1,"lab_id":lab_id,"user_id":user_id,"link":link,
			"comment_list":temp8})

def save_sharelink(request,lab_id):
	url=request.POST.get('url', "");
	user_id=request.POST.get('user_id', 0);
	user_id = int(user_id)
	dele = Share_link.objects.all().filter(Share_user_id = user_id,Share_lab_id = lab_id)
	if dele.exists():
		dele.delete()
	adder = Share_link(
			Share_user_id = user_id,
			Share_lab_id = lab_id,			
			Share_url = url,
	        )                
	adder.save() 
	return redirect(reverse('workspace',args=(lab_id,)))

# return  HttpResponseRedirect(reverse('urlname'))
#return render(request, "regis/index.html",{'courses':data,"data2":data2,"year":year,"a1":a1,"a2":a2})

		