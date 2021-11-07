from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Proflie(models.Model):
	user = models.OneToOneField(User,null=True,on_delete=models.CASCADE)
	faculty = models.CharField(max_length=200,null=True)
	major =  models.CharField(max_length=200,null=True)


	

