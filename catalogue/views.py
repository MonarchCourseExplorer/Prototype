from django.shortcuts import render
from django.http import HttpResponseRedirect

from .models import MCEQuestions, MCEAnswer, MCEUserResponse, MCERecommendation
from .forms import FeedbackForm



# MCE Recommendations Quiz Page
def quiz_question(request, question_id):
    question = MCEQuestions.objects.get(pk=question_id)
    answers = MCEAnswer.objects.filter(question=question)
    return render(request, 'MCEQuiz/RecQuestion.html', {'question': question, 'answers': answers})

#def submit_answer(request):
 #   if request.method == 'POST':

#def show_recomendation(request): 

#MCE Feedback
def provideFeedback(request):
    submitted = False
    if request.method == "POST":
        form = FeedbackForm(request.POST)
        if form.is_valid():
            form.save()
            #Redirect user back to feedback page. --look into how to output feedback
            return HttpResponseRedirect('/provideFeedback?submitted=True') 
        else:
            form = FeedbackForm
            if 'submitted' in request.GET:
                submitted = True
    form = FeedbackForm
    return render(request, 'pages/provideFeedback.html', {'form':form, 'submitted':submitted})
