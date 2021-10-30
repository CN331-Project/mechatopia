from django.shortcuts import redirect, render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.models import User,auth
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

	return render(request, "learning_article.html",{'link':link})

# return  HttpResponseRedirect(reverse('urlname'))




