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
    class Meta:
        model = Feedback
        fields = "__all__"

        widgets = {
            'section_id': forms.TextInput(attrs={'placeholder':'Enter course number here'}),
            'subject': forms.TextInput(attrs={'placeholder':'Enter subject here'}),
            'semester': forms.TextInput(attrs={'placeholder':'Enter semester along with the year. i.e. (Fall 2020)'}),
            'professor_id': forms.TextInput(attrs={'placeholder':'Enter professor name here'}),
            'review': forms.TextInput(attrs={'placeholder':'Please share some of your thoughts about the instructor.'}),
            'difficulty_rating': forms.TextInput(attrs={'placeholder':'Enter an integer between 1 and 5'}),
            'workload_rating': forms.TextInput(attrs={'placeholder':'Enter an integer between 1 and 5'}),
            'openness_rating': forms.TextInput(attrs={'placeholder':'Enter an integer between 1 and 5'}),
        }


# class RecommendationForm(forms.ModelForm):
#     class Meta:
#         model = recCombined
#         fields = "__all__"      