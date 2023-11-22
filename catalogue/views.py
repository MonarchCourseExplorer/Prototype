from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from .forms import SyllabusForm
from .models import MCEQuestions, MCEAnswer, MCEUserResponse, MCERecommendation
from .forms import FeedbackForm

def success(request):
    return render(request,'pages/success.html')

def upload_Syllabus(request): 
    
    if request.method == 'POST':
        form = SyllabusForm(request.POST, request.FILES)
        #file = request.FILES['file']
        if form.is_valid():
            form.save()

            #syllabus_instance =form.save()
            # Update the text_content
            #update_syllabus_text_content(syllabus_instance.id)
            return redirect('success')
    else:
        form = SyllabusForm()


    
    return render(request, 'pages/upload.html', {'form': form})

# MCE Recommendations Quiz Page
def quiz_question(request, question_id):
    question = MCEQuestions.objects.get(pk=question_id)
    answers = MCEAnswer.objects.filter(question=question)
    return render(request, 'MCEQuiz/RecQuestion.html', {'question': question, 'answers': answers})

#def submit_answer(request):
 #   if request.method == 'POST':

#def show_recomendation(request): 

#MCE Feedback
def add_feedback(request):
    submitted = False
    if request.method == "POST":
        form = FeedbackForm(request.POST)
        if form.is_valid():
            form.save()
            #Redirect user back to feedback page. --look into how to output feedback
            return HttpResponseRedirect('/add_feedback?submitted=True') 
        else:
            form = FeedbackForm
            if 'submitted' in request.GET:
                submitted = True
    form = FeedbackForm
    return render(request, 'Feedback/UserFeedback.html', {'form':form, 'submitted':submitted})