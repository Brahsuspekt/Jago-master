from django.contrib import admin
from .models import Department, Program, Course, SharedFile
# Register your models here.

admin.site.register(Department)
admin.site.register(Program)
admin.site.register(Course)
admin.site.register(SharedFile)
