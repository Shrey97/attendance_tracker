from django.contrib import admin
from .models import student, course, prof, attn
# Register your models here.
admin.site.register(student)
admin.site.register(course)
admin.site.register(prof)
admin.site.register(attn)
