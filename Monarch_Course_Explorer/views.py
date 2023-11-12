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