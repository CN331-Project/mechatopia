from django.shortcuts import redirect, render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.models import User,auth
import pandas as pd
import numpy as np
#from .models import Course
#from users.models import Student

# Create your views here.


def learning(request):
    return render(request, "search_learning.html")
    
def articles(request,learning_id):
	link ="0"
	if learning_id == 1 :
		link = "http://marcuscode.com/lang/python/introduction"
	elif learning_id == 2 :
		link = "http://marcuscode.com/lang/python/installing-python"
	elif learning_id == 3 :
		link = "http://marcuscode.com/lang/python/selection-statements"

#	url='https://drive.google.com/file/d/0B6GhBwm5vaB2ekdlZW5WZnppb28/view?usp=sharing'
#	url='https://docs.google.com/spreadsheets/d/1HlChpGDxiAxjMy6U9abRVjpOFT2nWhso045oEmKphGI/edit?usp=sharing'	
#	url2='https://drive.google.com/uc?id=' + url.split('/')[-2]
#	df = pd.read_csv(url) """
#https://docs.google.com/spreadsheets/d/1A5Djfc0WdMxa6d_Fm3qCTLnwm1b3Flpro_kZ0-sOEjQ/edit?usp=sharing
	test = pd.read_csv("https://docs.google.com/spreadsheets/d/"+"1A5Djfc0WdMxa6d_Fm3qCTLnwm1b3Flpro_kZ0-sOEjQ"+"/export?format=csv")
				#+"/export?format=csv",index_col=0,parse_dates=['Quradate'])
                   # Set first column as rownames in data frame             
                   # Parse column values to datetime            
                  #https://docs.google.com/spreadsheets/d/1HlChpGDxiAxjMy6U9abRVjpOFT2nWhso045oEmKphGI/export?format=csv
	x = test.head()  
	null_df = pd.DataFrame([],[])
	#for i in range(6):
#	a = x.loc[2][2] # 1คะแนน 2user 3pass
	b = x.loc[x['username'] == "toby"]
	c = b.loc[b['password'] == "1234"]
	#gg = test.head(3).split("\n")
	y = c.to_numpy()
#	yy = y[y.len()-1]
	score = 000
	return render(request, "learning_article.html",{'link':link,'df':y,'score':score})

# return  HttpResponseRedirect(reverse('urlname')) c.loc[c.username[1]][2]




