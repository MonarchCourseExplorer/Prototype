from django import forms
from django.forms import ModelForm
from .models import Syllabus
from .models import Section
from .models import Feedback
#from .models import MCERecommendation
#from .models import recAnswer
# from .models import recquestions
#from .models import recCombined

class SyllabusForm(ModelForm):
    sections = Section.objects.filter(semester="202310").filter(course__department="CS").order_by("course__number")
    section = forms.ModelChoiceField(sections, to_field_name="id")
    
    class Meta:
        model = Syllabus
        #field = "__all__"   gets all fields from user
        fields = ('class_name', 'section', 'original_location') 
    #orginal_location = forms.FileField(widget=forms.FileInput())

    
#Create Section Form
class SectionForm(ModelForm):
    class Meta:
        model = Section
        fields = "__all__"


class FeedbackForm(ModelForm):
    sections = Section.objects.filter(semester="202310").filter(course__department="CS").order_by("course__number")
    section = forms.ModelChoiceField(sections, to_field_name="id")

    class Meta:
        model = Feedback
        fields = "__all__"

        widgets = {
            'review': forms.TextInput(attrs={'placeholder':'Please share some of your thoughts about the instructor.'}),
            'difficulty_rating': forms.TextInput(attrs={'placeholder':'Enter an integer between 1 and 5'}),
            'workload_rating': forms.TextInput(attrs={'placeholder':'Enter an integer between 1 and 5'}),
            'openness_rating': forms.TextInput(attrs={'placeholder':'Enter an integer between 1 and 5'}),
        }


# class RecommendationForm(forms.ModelForm):
#     class Meta:
#         model = recCombined
#         fields = "__all__"      
