from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from .forms import SyllabusForm

from .models import recQuestions, recAnswer, MCERecommendation
from .forms import FeedbackForm


def success(request):
    return render(request,'pages/success.html')


# Recommendations Quiz Page
def quiz_view(request):
    if request.method == 'POST':
        for question_id, choice in request.POST.items():
            if question_id.startswitch('questions_text'):
                quiz_id = question_id.spilt('_')[1]
                question = recQuestions.objects.get(id=quiz_id)
                recAnswer.objects.create(question=question, choice=choice)

        return redirect('results') #This redirects to another page called "Results" or can be changed to another view name
    
    quizzes = recQuestions.objects.all()
    return render(request, 'RecQuestion.html', {'quizzes': quizzes})

def generate_recommendations(answers): 
    # The answer being the course the user entered
    user_course = answers[0].choice
    # Retrieves the recommendation for the users' entered course
    recommendations = MCERecommendation.objects.filter(course=user_course)
    # Converts queryset to a list
    recommendations_list = list(recommendations.values())
    return recommendations_list

def quiz_view(request):
    if request.method == 'POST':
        answers = []
        for question_id, choice in request.POST.items():
            if question_id.startswitch('questions_text_'):
                quiz_id = question_id.spilt('_')[1]
                question = recQuestions.objects.get(id=quiz_id)
                answer = recAnswer(question=question, choice=choice)
                answers.append(answer)
        
        recommendations = generate_recommendations(answers)

        # Saving the recommendations to the Database
        for recommendation in recommendations:
            MCERecommendation.objects.create(title=recommendation['title'],
                                             content=recommendation['content'],
                                             course=answers[0].choice)

        return render(request, 'results.html', {'recommendations': recommendations})
    
    quizzes = recQuestions.objects.all()
    return render(request, 'RecQuestion.html', {'quizzes': quizzes})
  

def upload_Syllabus(request): 
    
    if request.method == 'POST':
        form = SyllabusForm(request.POST, request.FILES)
        #file = request.FILES['file']
        if form.is_valid():
            form.save()
            return redirect('success')
    else:
        form = SyllabusForm()
    
    return render(request, 'pages/upload.html', {'form': form})


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
