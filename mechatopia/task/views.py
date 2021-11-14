from django.shortcuts import redirect, render
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.models import User,auth
from task.models import Challenge,Challenge_test_case,Challenge_tag
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
	if request.method == 'POST' and request.FILES['mycode']:
		myfile = request.FILES['mycode']
		fs = FileSystemStorage()
		name = "code_" + "1" + "_" + str(challenge_id)

		if os.path.isfile("file/" + code_st_path + name + ".txt"):
			os.remove("file/" + code_st_path + name + ".txt")  

		filename = fs.save(code_st_path + name + ".txt" , myfile)
		uploaded_file_url = fs.url(filename)
		return redirect(reverse('problem',args=(challenge_id,)))
	else:
		return redirect(reverse('problem',args=(challenge_id,)))
	return redirect(reverse('problem',args=(challenge_id,)))

def simple_upcode(request,challenge_id):
	code_st_path = "challenge_code/"
	code_box = request.POST.get('code_box', False);
	if request.method == 'POST':
		name = "code_" + "1" + "_" + str(challenge_id)
		code_file = "file/" + code_st_path + name + ".txt"
		if os.path.isfile(code_file):
			os.remove(code_file)  

		file1 = open(code_file,"w")
		file1.write("".join(code_box.split("\n")))
	#	file1.writelines(lines3)
		file1.close()
		return redirect(reverse('problem',args=(challenge_id,)))
	return redirect(reverse('problem',args=(challenge_id,)))
			
"""

	a1=''
    a2=0
    a1=request.POST.get('a1', '');
    a2=request.POST.get('a2', 0);
    temp3 = 0
    year = 0
    temp = User.objects.all().filter(id=request.user.id)
    temp4 = Student.objects.all().filter(STID=request.user.id)
    temp2 = temp4.values_list('college_year')
    if temp2: 
        temp3 = int(temp2[0][0])
    if temp3:
        year = temp3
        data = Course.objects.exclude(student=request.user.id).filter(for_year=year)
    else:
        data = Course.objects.exclude(student=request.user.id) #.filter(year=year[0][0]) # เอาช่อง isstaffเก็บชั้นปีละกัน
    data2 = Course.objects.all()
    if a2!= '0' and a1 != '':
       data2 = Course.objects.all().filter(c_code=a1,for_year=a2)
    elif a2!='0':
       data2 = Course.objects.all().filter(for_year=a2)
    elif a1 != '':
       data2 = Course.objects.all().filter(c_code=a1)


    return render(request, "regis/index.html",{'courses':data,"data2":data2,"year":year,"a1":a1,"a2":a2})

"""
def problem(request,challenge_id):
	user_id = 1
	link = ""
	temp = Challenge.objects.all().filter(Challenge_ID = challenge_id)
	if challenge_id == 1:
		link = "https://programming.in.th/task/rev2_problem.php?pid=0000"
	elif challenge_id == 2:
		link = "https://programming.in.th/task/rev2_problem.php?pid=0002"
	elif challenge_id == 3:
		link = "https://programming.in.th/task/rev2_problem.php?pid=0009";

	temp2 = Challenge_test_case.objects.all().filter(Challenge_test_challenge_id = challenge_id).values_list()
	path_test = "static/challenge/challenge_test/"
	path_answer = "static/challenge/challenge_answer/"
	path_py = "file/challenge_code/temp_py/"
	path_code = "file/challenge_code/"
	file_test = open(os.path.join(settings.BASE_DIR, path_test + temp2[0][4] +".txt"))
	file_answer = open(os.path.join(settings.BASE_DIR, path_answer + temp2[0][5] +".txt"))
	file_code = os.path.join(settings.BASE_DIR, path_code + "code_1_" + str(challenge_id) +".txt")
	score = 0
	correct = 0
	count = 0
	output = ""
	lines4 = ""
	for i in temp2:
		count+=1
		with open(os.path.join(settings.BASE_DIR, path_test + i[4] +".txt")) as f:
			lines1 = f.read()

		with open(os.path.join(settings.BASE_DIR, path_answer + i[5] +".txt")) as f:
			lines2 = f.read()


		if os.path.isfile(file_code):
			with open(os.path.join(file_code)) as f:
				lines4 = f.read()

			lines3 = []
			with open(os.path.join(file_code)) as f:
				lines3 = f.readlines()
			for j in range(len(lines3)):
				lines3[j] = lines3[j].replace("input()","sys.argv[" + "next(counter)" + "]")

			temp_py_file = os.path.join(settings.BASE_DIR, path_py + "code_1_" + str(challenge_id) +".py")
			file1 = open(temp_py_file,"w")
			file1.write("from itertools import count \n")
			file1.write("import sys \n")
			file1.write("counter = count(1) \n")
			#file1.write("print(sys.argv[1]) \n")
			file1.writelines(lines3)
			file1.close()

			#run = "python " + temp_py_file + " " + " ".join(lines1.split("\n")) + " \n "
			run = "python " + temp_py_file + " " + " ".join(lines1.split("\n")) + " \n "
			
			p = subprocess.Popen([run], stdout=subprocess.PIPE)
			output = p.communicate()[0].decode()

			if lines2.split() == output.split():
				correct+=1
				score+=i[3]
	return render(request, "problem.html",{'link':link,'query':temp,'user_id':user_id,'challenge_id':challenge_id,
				'temp2':lines1.split("\n"),'temp3':output.split(),'temp4':lines2.split(),"score":score,"code_box":lines4,
				"score":score,"count":count,"correct":correct})     
      


def lab(request):
    return render(request, "tem.html")



# return  HttpResponseRedirect(reverse('urlname'))
#return render(request, "regis/index.html",{'courses':data,"data2":data2,"year":year,"a1":a1,"a2":a2})


