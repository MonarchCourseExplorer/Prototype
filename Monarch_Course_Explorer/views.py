from django.shortcuts import render
from django.http import HttpResponseRedirect
from catalogue.forms import FeedbackForm


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