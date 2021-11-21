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
from admin_edit import views as views4
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('admin/', admin.site.urls),
    path('about/',views1.about),
### users
    path('', views1.welcome, name='index'),
    path('tem/', views1.tem, name='tem'),
    path('dashboard/', views1.dashboard,name='dashboard'),    
    path('login/',views1.login, name="login"),
    path('check_login/',views1.check_login, name="check_login"),
    path('logout/',views1.logout, name="logout"),
    path('signup/',views1.signup, name="signup"),
    path('signupform/',views1.signupform, name="signupform"),    

### learning
	path('learning/', views2.learning ,name='learning'),
	path('learning/articles/<int:learning_id>/', views2.articles ,name='articles'),
    path('learning_bak/', views2.learning_bak ,name='learning_bak'),
    path('comment/<int:object_id>/<int:object_is>/', views2.comment ,name='comment'),

### task
    path('lab/', views3.lab ,name='lab'),
    path('lab/workspace/<int:lab_id>/', views3.workspace ,name='workspace'),
    path('challenge/', views3.challenge ,name='challenge'),
    path('challenge/problem/<int:challenge_id>/', views3.problem ,name='problem'),
    path('simple_upload/<int:challenge_id>/', views3.simple_upload ,name='simple_upload'),
    path('simple_upcode/<int:challenge_id>/', views3.simple_upcode ,name='simple_upcode'),
    path('save_sharelink/<int:lab_id>/', views3.save_sharelink ,name='save_sharelink'),

### admin_add/edit
    path('admin_dashboard/', views4.admin_dashboard,name='admin_dashboard'),
    path('admin_add_tag/<int:have_message>/', views4.admin_add_tag,name='admin_add_tag'),
    path('admin_add_tag_p/', views4.admin_add_tag_p,name='admin_add_tag_p'),
    path('admin_add_lesson_group/<int:have_message>/', views4.admin_add_lesson_group,name='admin_add_lesson_group'),
    path('admin_add_lesson_group_p/', views4.admin_add_lesson_group_p,name='admin_add_lesson_group_p'),
    path('admin_add_lesson/<int:have_message>/', views4.admin_add_lesson,name='admin_add_lesson'),
    path('admin_add_lesson_p/', views4.admin_add_lesson_p,name='admin_add_lesson_p'),
    path('admin_add_lab/<int:have_message>/', views4.admin_add_lab,name='admin_add_lab'),
    path('admin_add_lab_p/', views4.admin_add_lab_p,name='admin_add_lab_p'),
    path('admin_add_challenge/<int:have_message>/', views4.admin_add_challenge,name='admin_add_challenge'),
    path('admin_add_challenge_p/', views4.admin_add_challenge_p,name='admin_add_challenge_p'),
    path('admin_add_testcase/<int:have_message>/', views4.admin_add_testcase,name='admin_add_testcase'),
    path('admin_add_testcase_p/', views4.admin_add_testcase_p,name='admin_add_testcase_p'),
    path('admin_add_testcase_pp/', views4.admin_add_testcase_pp,name='admin_add_testcase_pp'),
    path('admin_add_assignment/<int:have_message>/', views4.admin_add_assignment,name='admin_add_assignment'),
    path('admin_add_assignment_p/', views4.admin_add_assignment_p,name='admin_add_assignment_p'),
    path('admin_add_assignment_pp/', views4.admin_add_assignment_pp,name='admin_add_assignment_pp'),

]

urlpatterns += staticfiles_urlpatterns()

### path('login/', views1.login),
### path('login/check_login/', views1.check_login),
### path('logout/',views1.logout),
### path('signup',views1.signup),
### path('signup/check_signup', views1.check_signup),
### path('success01/<int:page_id>/<int:status>/', views1.succes01),
### each_article
#   path('task/lab/', views3.lab ,name='lab'),