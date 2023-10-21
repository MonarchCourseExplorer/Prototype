from django.contrib import admin
from .models import Course
from .models import Section
from .models import Syllabus
from .models import Feedback

# Register your models here.
admin.site.register(Course)
admin.site.register(Section)
admin.site.register(Syllabus)
admin.site.register(Feedback)