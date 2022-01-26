from django.contrib import admin

# Register your models here.
from .models import  User,Progress,Code,Pass,Share_link


admin.site.register(User)
admin.site.register(Progress)
admin.site.register(Code)
admin.site.register(Pass)
admin.site.register(Share_link)


