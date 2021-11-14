"""mechatopia URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from learning import views as views2
from users import views as views1
from task import views as views3
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('admin/', admin.site.urls),



### users
    path('', views1.welcome, name="welcome"),
    path('home/', views2.home, name="home"),
    path('challenge/', views3.challenge, name="challenge"),
    path('challenge/x', views3.challengeX, name="challengeX"),
    path('home/task', views3.lab, name="task"),
    path('setting/', views1.setting, name="setting"),
    path('progress/', views2.progress, name="progress"),


    path('loginform', views1.loginform, name="login"),
    path('logout', views1.logout, name="logout"),
    path('signup', views1.signup, name="signup"),
    path('signupform', views1.account, name="signupform"),

    path('editprofile', views1.editprofile, name="editprofile"),


]

urlpatterns += staticfiles_urlpatterns()
