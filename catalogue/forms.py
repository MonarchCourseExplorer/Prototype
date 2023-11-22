from django import forms
from django.forms import ModelForm
from .models import Syllabus
from .models import Section
from .models import Feedback

class SyllabusForm(ModelForm):
    class Meta:
        model = Syllabus
        #field = "__all__"   gets all fields from user
        fields = ('class_name','file')
        
    file = forms.FileField(widget=forms.FileInput())
    
#Create Section Form
class SectionForm(ModelForm):
    class Meta:
        model = Section
        fields = "__all__"


class FeedbackForm(ModelForm):
    class Meta:
        model = Feedback
        fields = ('Subject', 'SectionID', 'ProfessorID', 'Semester', 'Review')

        
