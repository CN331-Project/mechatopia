from django.contrib import admin

# Register your models here.

from .models import  Lesson,Lesson_group,Assignment,Comment


admin.site.register(Lesson)
admin.site.register(Lesson_group)
admin.site.register(Assignment)
admin.site.register(Comment)
