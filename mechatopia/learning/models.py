from django.db import models

# Create your models here.


class Lesson(models.Model):
	Lesson_ID = models.BigAutoField(auto_created=True, primary_key=True)
	Lesson_name = models.CharField(max_length=200 ,null=True)
	Lesson_description = models.TextField(null=True)
	Lesson_link = models.TextField(null=True)
	Lesson_date = models.CharField(max_length=15 ,null=True)
	Lesson_admin_add = models.IntegerField(null=True)
	Lesson_group_id = models.IntegerField(null=True)

class Lesson_group(models.Model):
	Lesson_group_ID = models.BigAutoField(auto_created=True, primary_key=True)
	Lesson_group_name = models.CharField(max_length=200 ,null=True)
	Lesson_group_description = models.TextField(null=True)
	Lesson_group_admin_add = models.IntegerField(null=True)
	Lesson_group_recent_date = models.CharField(max_length=15 ,null=True)
	Lesson_group_pic = models.CharField(max_length=200 ,null=True)

class Assignment(models.Model):
	Assignment_ID = models.BigAutoField(auto_created=True, primary_key=True)
	Assignment_lesson_id = models.IntegerField(null=True)
	Assignment_test = models.CharField(max_length=200 ,null=True) # ไม่แน่ใจ
	Assignment_answer = models.CharField(max_length=200 ,null=True) #

class Comment(models.Model):
	Comment_ID = models.BigAutoField(auto_created=True, primary_key=True)
	Comment_lesson_id = models.IntegerField(null=True)
	Comment_user_id = models.IntegerField(null=True)
	Comment_text = models.TextField(null=True)
	comment_reply = models.IntegerField(null=True)




