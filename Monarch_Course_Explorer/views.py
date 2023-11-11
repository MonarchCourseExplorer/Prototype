from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from catalogue.models import Course

# Render the Monarch Course Explorer home page
def homeView(request):
    mydata = Course.objects.all().distinct('department').order_by('department')
    template = loader.get_template('index.html')
    context = {
        'departments': mydata
    }

    return HttpResponse(template.render(context, request))

# Render gallery page
def galleryView(request):
    return render(request, 'pages/gallery.html')

# Render the provideFeedback page
def provideFeedbackView(request):
    return render(request, 'pages/provideFeedback.html')