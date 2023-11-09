from django.shortcuts import render

# Render the Monarch Course Explorer home page
def homeView(request):
    return render(request, 'index.html')

# Render gallery page
def galleryView(request):
    return render(request, 'pages/gallery.html')

# Render the provideFeedback page
def provideFeedbackView(request):
    return render(request, 'pages/provideFeedback.html')