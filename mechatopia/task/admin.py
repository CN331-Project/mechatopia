from django.contrib import admin

# Register your models here.
from .models import  Challenge,Challenge_test_case,Challenge_tag,Lab,Lab_tag,Lab_in_tag,Challenge_in_tag


admin.site.register(Challenge)
admin.site.register(Challenge_test_case)
admin.site.register(Challenge_tag)
admin.site.register(Lab)
admin.site.register(Lab_tag)
admin.site.register(Lab_in_tag)
admin.site.register(Challenge_in_tag)