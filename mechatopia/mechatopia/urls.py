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
   
    path('dashboard/', views1.dashboard,name='dashboard'),
    path('tem/', views1.tem ,name='tem'),
    
    
    path('', views1.welcome),
    path('loginform',views1.loginform, name="login"),
    path('logout',views1.logout, name="logout"),
    path('signup',views1.signup, name="signup"),
    path('signupform',views1.account, name="signupform"),
    
### path('login/', views1.login),
### path('login/check_login/', views1.check_login),
### path('logout/',views1.logout),
### path('signup',views1.signup),
### path('signup/check_signup', views1.check_signup),
### path('success01/<int:page_id>/<int:status>/', views1.succes01),

### learning
	path('learning/', views2.learning ,name='learning'),
	path('learning/articles/<int:learning_id>/', views2.articles ,name='articles'),
### task
	path('task/challenge/', views3.challenge,name='challenge'),
    path('task/lab/', views3.lab ,name='lab'),
    path('learning_bak/', views2.learning_bak ,name='learning_bak'),
    

### each_article
#	path('task/lab/', views3.lab ,name='lab'),
]

urlpatterns += staticfiles_urlpatterns()