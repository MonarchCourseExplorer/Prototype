from django.contrib import admin
from .models import Course
from .models import Section
from .models import Syllabus
from .models import Feedback
from .models import MCEQuestions
from .models import MCEAnswer
from .models import MCEUserResponse
from .models import MCERecommendation

# Register your models here.
admin.site.register(Course)
admin.site.register(Section)
admin.site.register(Syllabus)
admin.site.register(Feedback)
admin.site.register(MCEQuestions)
admin.site.register(MCEAnswer)
admin.site.register(MCEUserResponse)
admin.site.register(MCERecommendation)