from django.contrib import admin
from .models import Student
from .models import Professor

# Register your models here.
admin.site.register(Student)
admin.site.register(Professor)