from django.shortcuts import render
from .models import MCEQuestions, MCEAnswer, MCEUserResponse, MCERecommendation

# MCE Recommendations Quiz Page
def quiz_question(request, question_id):
    question = MCEQuestions.objects.get(pk=question_id)
    answers = MCEAnswer.objects.filter(question=question)
    return render(request, 'MCEQuiz/RecQuestion.html', {'question': question, 'answers': answers})

#def submit_answer(request):
 #   if request.method == 'POST':

#def show_recomendation(request): 
