from django.shortcuts import render
from django.conf import settings

# Render the Monarch Course Explorer home page
def homeView(request):
    return render(request, 'index.html')

# Render gallery page
def galleryView(request):
    return render(request, 'pages/gallery.html')

# Render the Monarch Course Explorer quiz page
def quizView(request):
    return render(request, str(settings.CATALOGUE_DIR) + '/RecQuestion.html')

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