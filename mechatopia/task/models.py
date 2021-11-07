from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Lab(models.Model):
	Lab_name = models.CharField(max_length=200 ,null=True)
	Lab_detail = models.CharField(max_length=200 ,null=True)
	def __str__(self):
    		return f"{self.Lab_name}"
	
	
class Lab_tag(models.Model):
	Lab_user = models.OneToOneField(User,null=True,on_delete=models.CASCADE)
	Lab_select = models.OneToOneField(Lab,null=True,on_delete=models.CASCADE)
	score = models.IntegerField(null=True,blank=True)

	def __str__(self):
    		return f"{self.Lab_user.first_name} {self.Lab_user.last_name} {self.Lab_select}"



