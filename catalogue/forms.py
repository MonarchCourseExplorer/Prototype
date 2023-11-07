"""
from django import forms
from django.forms import ModelForm
from .models import Syllabus


#Create Syllabus form
class SyllabusForm(ModelForm):
    class Meta:
        model = Syllabus
        #field = "__all__"   gets all fields from user
        field = ()


"""