from django.contrib import admin

# Register your models here.
from .models import  Lab,Lab_tag

admin.site.register(Lab)
admin.site.register(Lab_tag)
