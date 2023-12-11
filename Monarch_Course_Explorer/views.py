from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from catalogue.forms import FeedbackForm
from catalogue.models import Semester, Department, Course, Feedback, Syllabus
from django.db import connection
from .forms import CourseSearchForm
from urllib import parse


# Render the Monarch Course Explorer home page
def homeView(request):
    if request.method == "POST":
        searchForm = CourseSearchForm(request.POST)
        if searchForm.is_valid():
            data = searchForm.cleaned_data
            print(parse.quote(data['search']))
            return redirect('pages/searchResults.html?semester={0}&subject={1}&search={2}'.format(data['semester'].short_name, data['department'].abbreviation, parse.quote(data['search'])))
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
                           section.id, section.delivery_type, section.offering_days, section.offering_time,
                           prof.first_name, prof.last_name
                    FROM catalogue_course AS course INNER JOIN catalogue_section AS section ON course.id = section.course_id
                        INNER JOIN users_professor AS prof ON section.professor_id = prof.id
                    WHERE course.department = %(subject)s AND section.semester = %(semester)s
                        AND (course.number ILIKE '%%' || %(search)s || '%%' OR prof.first_name || prof.last_name ILIKE '%%' || %(search)s || '%%');"""
        
        cur.execute(strSQL, {'subject': request.GET['subject'], 'semester': request.GET['semester'], 'search': parse.unquote(request.GET['search'])})
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
    allSelectedFeedback = [] # All of the feedback for the selected course
    #Again, screw django's ORM
    strFrom = """SELECT course.department, course.number, course.name, 
                                section.semester, section.delivery_type, section.offering_days, section.offering_time,
                                semester.friendly_name,
                                feedback.difficulty_rating, feedback.workload_rating, feedback.openness_rating, feedback.review,
                                prof.first_name, prof.last_name
                           FROM catalogue_course AS course INNER JOIN catalogue_section AS section ON course.id = section.course_id
                                INNER JOIN catalogue_semester AS semester ON section.semester = semester.short_name
                                INNER JOIN users_professor AS prof ON section.professor_id = prof.id
                                INNER JOIN catalogue_feedback AS feedback ON section.id = feedback.section_id """
    strOrder = "ORDER BY section.semester, prof.last_name, prof.first_name, section.delivery_type, section.offering_time, section.offering_time;"

    if request.method == "POST":
        requestPost = request.POST

        if 'courseSelect' in requestPost: # Check if any feedback has been submitted about the selected course
            with connection.cursor() as cur:
                strSQL = strFrom + "WHERE course.id = %s " + strOrder
        
                cur.execute(strSQL, (request.POST['courseSelect'], ))
                allSelectedFeedback = dictfetchall(cur)
    elif request.method == "GET":
        if 'id' in request.GET:
            with connection.cursor() as cur:
                strSQL = strFrom + "WHERE section.id = %s " + strOrder
        
                cur.execute(strSQL, (request.GET['id'], ))
                allSelectedFeedback = dictfetchall(cur)

    return render(request, 'pages/browseFeedback.html', {"allCourses": Course.objects.all().order_by('department', 'number'), "allSelectedFeedback": allSelectedFeedback})

# Render the syllabus page
def provideSyllabusView(request):
    data = []

    strFrom = """SELECT course.department, course.number, course.name, Syllabus.class_name, Syllabus.syllabus_contents,
                        section.semester, section.delivery_type, section.offering_days, section.offering_time,
                        semester.friendly_name
                FROM catalogue_course AS course 
                INNER JOIN catalogue_section AS section ON course.id = section.course_id
                INNER JOIN catalogue_Syllabus as Syllabus ON course.id = section.course_id 
                INNER JOIN users_professor AS prof ON section.professor_id = prof.id """

    strOrder = "ORDER BY section.semester, prof.last_name, prof.first_name, section.delivery_type, section.offering_time, section.offering_time;"

    if request.method == "POST":
        requestPost = request.POST

        if 'courseSelect' in requestPost:
            with connection.cursor() as cur:
                strSQL = strFrom + "WHERE course.id = %s " + strOrder

                cur.execute(strSQL, (request.POST['courseSelect'], ))
                data = dictfetchall(cur)
    elif request.method == "GET":
        if 'id' in request.GET:
            with connection.cursor() as cur:
                strSQL = strFrom + "WHERE section.id = %s " + strOrder

                cur.execute(strSQL, (request.GET['id'], ))
                data = dictfetchall(cur)
        else:
            # If there's no specific ID, don't include the WHERE clause
            with connection.cursor() as cur:
                strSQL = strFrom + strOrder

                cur.execute(strSQL)
                data = dictfetchall(cur)

    return render(request, 'pages/syllabus.html', {"allCourses": Course.objects.all().order_by('department', 'number'), 'data': data})
#Render the Register page
def provideRegisterView(request):
    return render(request, '../../users/templates/authenticate/register.html')

# Render the student login page
def provideStudentLoginView(request):
    return render(request, '../../users/templates/authenticate/login.html')

# Render the faculty login page
def provideFacultyLoginView(request):
    return render(request, '../../users/templates/authenticate/faculty_login.html')

# Render the success page
def successView(request):
    return render(request, 'pages/success.html')

def dictfetchall(cursor):
    """
    Return all rows from a cursor as a dict.
    Assume the column names are unique.
    Pulled from https://docs.djangoproject.com/en/4.2/topics/db/sql/
    """
    columns = [col[0] for col in cursor.description]
    return [dict(zip(columns, row)) for row in cursor.fetchall()]

def syllabusView(request):
    return render(request, '/media/documents/CS300T_Syllabus.pdf')
