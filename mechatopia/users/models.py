from django.db import models

# Create your models here.

class User(models.Model):
	User_ID = models.BigAutoField(auto_created=True, primary_key=True)
	User_username = models.CharField(max_length=200 ,null=True)
	User_password = models.CharField(max_length=200 ,null=True)
	User_email = models.CharField(max_length=200 ,null=True)
	User_is_admin = models.BooleanField(null=True)
	User_score = models.IntegerField(null=True)
	User_rank = models.CharField(max_length=200 ,null=True)
	User_pic = models.CharField(max_length=200 ,null=True)
	User_bio = models.TextField(null=True)

class Progress(models.Model):
	Progress_ID = models.BigAutoField(auto_created=True, primary_key=True)
	Progress_user_id = models.IntegerField(null=True)
	Progress_lesson_id = models.IntegerField(null=True)

class Code(models.Model):
	Code_ID = models.BigAutoField(auto_created=True, primary_key=True)
	Code_directory = models.CharField(max_length=200 ,null=True)
	Code_user_id = models.IntegerField(null=True)
	Code_challenge_id = models.IntegerField(null=True)

class Pass(models.Model):
	Pass_ID = models.BigAutoField(auto_created=True, primary_key=True)
	Pass_user_id = models.IntegerField(null=True)
	Pass_challenge_id = models.IntegerField(null=True)