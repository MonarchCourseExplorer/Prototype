from django.contrib import admin
from .models import Course
from .models import Section
from .models import Syllabus
from .models import Feedback
from .models import recQuestions
from .models import recAnswer
from .models import MCERecommendation
from .models import recCombined

# Register your models here.
admin.site.register(Course)
admin.site.register(Section)
admin.site.register(Syllabus)
admin.site.register(Feedback)
admin.site.register(recQuestions)
admin.site.register(recAnswer)
admin.site.register(MCERecommendation)
admin.site.register(recCombined)