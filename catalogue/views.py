from django.shortcuts import render, redirect
from .forms import SyllabusForm, FeedbackForm

# success for feedback
def success(request):
    return render(request,'pages/success.html')

# success for syllabus
def syllabusSuccess(request):
    return render(request,'pages/syllabusSuccess.html')

def uploadSyllabus(request): 
    
    if request.method == 'POST':
        form = SyllabusForm(request.POST, request.FILES)
        #file = request.FILES['file']
        if form.is_valid():
            form.save()
            return redirect('syllabusSuccess')
    else:
        form = SyllabusForm()
    
    return render(request, 'pages/upload.html', {'form': form})

"""
def uploadSyllabus(request): 
    
    if request.method == 'POST':
        form = SyllabusForm(request.POST, request.FILES)
        #file = request.FILES['file']
        if form.is_valid():
            form.save()
            return redirect('success')
    else:
        form = SyllabusForm()
    
    return render(request, 'pages/upload.html', {'form': form})
"""


# MCE Feedback
def provideFeedback(request):
    submitted = False
    if request.method == "POST":
        form = FeedbackForm(request.POST)
        if form.is_valid():
            form.save()
            # Redirect user back to feedback page. --look into how to output feedback
            # return HttpResponseRedirect('/provideFeedback?submitted=True')
            return redirect('success')
    else:

        form = FeedbackForm()
        if 'submitted' in request.GET:
            submitted = True
            
    #return render(request, 'provideFeedback.html', {'form':form, 'submitted':submitted})
    return render(request, 'pages/provideFeedback.html', {'form':form, 'submitted':submitted})

  
  
  
  # def upload_Syllabus(request): 
    
#     if request.method == 'POST':
#         form = SyllabusForm(request.POST, request.FILES)
#         #file = request.FILES['file']
#         if form.is_valid():
#             form.save()

#             #syllabus_instance =form.save()
#             # Update the text_content
#             #update_syllabus_text_content(syllabus_instance.id)
#             return redirect('success')
#     else:
#         form = SyllabusForm()

#     return render(request, 'pages/upload.html', {'form': form})
    