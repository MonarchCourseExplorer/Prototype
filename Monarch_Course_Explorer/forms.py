from django import forms
from catalogue.models import Semester, Department

class CourseSearchForm(forms.Form):
    semesters = Semester.objects.all().order_by('-short_name')
    departments = Department.objects.all().order_by('name')

    semester = forms.ModelChoiceField(semesters, 
                        empty_label="Semester",
                        to_field_name="short_name")
    department = forms.ModelChoiceField(departments,
                        empty_label="Subject",
                        to_field_name="abbreviation")
    search = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Search for a Course or a Professor'}))