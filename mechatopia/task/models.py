from django.db import models
from ckeditor.fields import RichTextField
# Create your models here.

class Challenge(models.Model):
	Challenge_ID = models.BigAutoField(auto_created=True, primary_key=True)
	Challenge_question = models.CharField(max_length=200 ,null=True)
	Challenge_file = models.CharField(max_length=200 ,null=True)
	Challenge_score = models.IntegerField(null=True)
	Challenge_level = models.IntegerField(null=True)
	Challenge_description = models.TextField(null=True)
	Challenge_date = models.CharField(max_length=15 ,null=True)
	Challenge_body = RichTextField()

class Challenge_test_case(models.Model):
	Challenge_test_ID = models.BigAutoField(auto_created=True, primary_key=True)
	Challenge_test_challenge_id = models.IntegerField(null=True)
	Challenge_test_no = models.IntegerField(null=True)
	Challenge_test_score = models.IntegerField(null=True)
	Challenge_test_test = models.TextField(null=True)
	Challenge_test_answer = models.TextField(null=True)

class Challenge_tag(models.Model):
	Challenge_tag_ID = models.BigAutoField(auto_created=True, primary_key=True)
	Challenge_tag_name = models.CharField(max_length=200 ,null=True)

class Lab(models.Model):
	Lab_ID = models.BigAutoField(auto_created=True, primary_key=True)
	Lab_name = models.TextField(null=True)
	Lab_link = models.TextField(null=True)
	Lab_description = models.TextField(null=True)
	Lab_pic = models.TextField(null=True)
	Lab_cover_pic = models.TextField(null=True)
	Lab_date = models.CharField(max_length=15 ,null=True)
	Lab_body = RichTextField()

class Lab_tag(models.Model):
	Lab_tag_ID = models.BigAutoField(auto_created=True, primary_key=True)
	Lab_name = models.CharField(max_length=200 ,null=True)

class Lab_in_tag(models.Model):
	Lab_in_tag_ID = models.BigAutoField(auto_created=True, primary_key=True)
	Lab_id = models.IntegerField(null=True)
	Lab_tag_id = models.IntegerField(null=True)

class Challenge_in_tag(models.Model):
	Challenge_in_tag_ID = models.BigAutoField(auto_created=True, primary_key=True)
	Challenge_id = models.IntegerField(null=True)
	Challenge_tag_id = models.IntegerField(null=True)