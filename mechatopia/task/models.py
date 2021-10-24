from django.db import models

# Create your models here.

class Challenge(models.Model):
	Challenge_ID = models.BigAutoField(auto_created=True, primary_key=True)
	Challenge_tag_id = models.IntegerField(null=True)
	Challenge_question = models.CharField(max_length=200 ,null=True)
	Challenge_description = models.TextField(null=True)
	Challenge_date = models.CharField(max_length=15 ,null=True)

class Challenge_test_case(models.Model):
	Challenge_test_ID = models.BigAutoField(auto_created=True, primary_key=True)
	Challenge_test_challenge_id = models.IntegerField(null=True)
	Challenge_test_no = models.IntegerField(null=True)
	Challenge_test_score = models.IntegerField(null=True)
	Challenge_test_test = models.TextField(null=True)
	Challenge_test_answer = models.TextField(null=True)

class Challenge_tag(models.Model):
	Challenge_tag_Id = models.BigAutoField(auto_created=True, primary_key=True)
	Challenge_name = models.CharField(max_length=200 ,null=True)

class Lab(models.Model):
	Lab_ID = models.BigAutoField(auto_created=True, primary_key=True)
	Lab_tag_id = models.IntegerField(null=True)
	Lab_link = models.TextField(null=True)
	Lab_question = models.TextField(null=True)

class Lab_tag(models.Model):
	Lab_tag_Id = models.BigAutoField(auto_created=True, primary_key=True)
	Lab_name = models.CharField(max_length=200 ,null=True)


