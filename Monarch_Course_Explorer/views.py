from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.conf import settings

from catalogue.forms import FeedbackForm
from catalogue.models import Semester, Department
from django.db import connection
from .forms import CourseSearchForm


# Render the Monarch Course Explorer home page
def homeView(request):
    if request.method == "POST":
        searchForm = CourseSearchForm(request.POST)
        if searchForm.is_valid():
            data = searchForm.cleaned_data
            return redirect('pages/searchResults.html?semester={0}&subject={1}&search={2}'.format(data['semester'].short_name, data['department'].abbreviation, data['search']))
    else:
        searchForm = CourseSearchForm()

    context = {
        'form': searchForm
    }

    return render(request, 'index.html', context)

def searchResultsView(request):
    #Could I have looked harder to figure out how to join catalogue and users? Yes. Am I going to? No.
    with connection.cursor() as cur:
        strSQL = """SELECT course.department, course.number, course.name, course.description,
                           section.id, section.crn,
                           prof.first_name, prof.last_name
                    FROM catalogue_course AS course INNER JOIN catalogue_section AS section ON course.id = section.course_id
                        INNER JOIN users_professor AS prof ON section.professor_id = prof.id
                    WHERE course.department = %(subject)s AND section.semester = %(semester)s
                        AND (course.number ILIKE '%%' || %(search)s || '%%' OR prof.first_name || prof.last_name ILIKE '%%' || %(search)s || '%%');"""
        
        cur.execute(strSQL, request.GET)
        results = dictfetchall(cur)

    return render(request, 'pages/searchResults.html', {'results': results})

def sectionView(request):
    return render(request, 'pages/viewSection.html')

# Render gallery page
def galleryView(request):
    return render(request, 'pages/gallery.html')

# Render the Monarch Course Explorer quiz page
def quizView(request):
    return render(request, 'pages/RecQuestion.html')

# Render the provideFeedback page
def provideFeedbackView(request):
    submitted = False
    if request.method == "POST":
        form = FeedbackForm(request.POST)
        print(request.POST)
        if form.is_valid():
            form.save()
            #Redirect user back to feedback page. --look into how to output feedback
            return HttpResponseRedirect('/provideFeedback?submitted=True')
    else:
        form = FeedbackForm()
        if 'submitted' in request.GET:
            submitted = True
            
    return render(request, 'pages/provideFeedback.html', {'form':form, 'submitted':submitted})

# Render the grades page
def provideGradesView(request):
    return render(request, 'pages/grades.html')

# Render the browse feedback page 
def provideBrowseFeedbackView(request):
    return render(request, 'pages/browseFeedback.html')

# Render the syllabus page
def provideSyllabusView(request):
    return render(request, 'pages/syllabus.html')

# Render the Register page
def provideRegisterView(request):
    return render(request, '../../users/templates/authenticate/register.html')

# Render the student login page
def provideStudentLoginView(request):
    return render(request, '../../users/templates/authenticate/login.html')

# Render the faculty login page
def provideFacultyLoginView(request):
    return render(request, '../../users/templates/authenticate/faculty_login.html')


def dictfetchall(cursor):
    """
    Return all rows from a cursor as a dict.
    Assume the column names are unique.
    Pulled from https://docs.djangoproject.com/en/4.2/topics/db/sql/
    """
    columns = [col[0] for col in cursor.description]
    return [dict(zip(columns, row)) for row in cursor.fetchall()]
