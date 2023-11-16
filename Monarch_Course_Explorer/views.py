from django.shortcuts import render
from django.conf import settings

# Render the Monarch Course Explorer home page
def homeView(request):
    return render(request, 'index.html')

# Render the Monarch Course Explorer home page when on the Login and Registration Pages
def homeViewFromLoginAndRegisterPages(request):
    return render(request, 'Monarch_Course_Explorer/templates/index.html')

# Render gallery page
def galleryView(request):
    return render(request, 'pages/gallery.html')

# Render the Monarch Course Explorer quiz page
def quizView(request):
    return render(request, 'pages/RecQuestion.html')
    # not sure how str(settings.CATALOGUE_DIR) works, seems to be messing with the rendering of the page.
    # return render(request, str(settings.CATALOGUE_DIR) + 'pages/RecQuestion.html')

# Render the provideFeedback page
def provideFeedbackView(request):
    return render(request, 'pages/provideFeedback.html')

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