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
from learning import views as views1
from users import views as views2
from task import views as views3

urlpatterns = [
    path('admin/', admin.site.urls),

]
"""
### users
    path('', views1.welcome),
    path('login/', views1.login),
    path('login/check_login/', views1.check_login),
    path('logout/',views1.logout),
    path('signup',views1.signup), 
    path('signup/check_signup', views1.check_signup),
    path('success01/<int:page_id>/<int:status>/', views1.succes01),

### learning

### task  

]



urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/<int:stid>/', views1.home),
    path('page1/', views1.page1),
    path('search_sub/<int:stid>/', views1.search_sub),
    path('home/adduser/', views1.adduser),
    path('home/adduser/adduser2/', views1.adduser2),
    path('success01/<int:stid>/<int:status>/', views1.succes01), """