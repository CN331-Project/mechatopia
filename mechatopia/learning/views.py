from django.shortcuts import render

# Create your views here.
from task.models import Lab

def home(request):
    lab = Lab.objects.all()
    return render(request,'home.html',{'labs':lab})

def progress(request):
    speak_time = [20,15,7,20,10,18,16,20,10,15]
    height = 200
    max_time = max(speak_time)
    percent_time_list = []
    for item in speak_time:
        percent_time = int((item/max_time) * height)
        percent_time_list.append(percent_time)

    all_list = zip(speak_time, percent_time_list)
    max_percent = (height * 80) / 100
    med_percent = (height * 40) / 100    
    return render(request,'progress.html',{'infors':all_list,'max':max_percent,'med':med_percent})

def setting(request):
   return render(request, "setting.html")
    