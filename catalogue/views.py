from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from .forms import SyllabusForm
# from .models import recquestions
#from .models import recAnswer 
#from .models import MCERecommendation
# from .forms import RecommendationForm
from .forms import FeedbackForm

def success(request):
    return render(request,'pages/success.html')

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
    
# Recommendations Quiz Page
# def generateRecommendations(answers): 
#     # The answer being the course the user entered
#     userCourse = answers[0].choice
#     # Retrieves the recommendation for the users' entered course
#     recommendations = MCERecommendation.objects.filter(course=user_course)
#     # Converts queryset to a list
#     recommendationsList = list(recommendations.values())
#     return recommendationsList

# def quizView(request):
#     if request.method == 'POST':
#         answers = []
#         for questionID, choice in request.POST.items():
#             if questionID.startswitch('questions_text_'):
#                 quizID = questionID.spilt('_')[1]
#                 question = recQuestions.objects.get(id=quizID)
#                 answer = recAnswer(question=question, choice=choice)
#                 answers.append(answer)
        
#         recommendations = generateRecommendations(answers)

#         # Saving the recommendations to the Database
#         for recommendation in recommendations:
#             MCERecommendation.objects.create(title=recommendation['title'],
#                                              content=recommendation['content'],
#                                              course=answers[0].choice)

#         return render(request, 'results.html', {'recommendations': recommendations})
    
#     quizzes = recQuestions.objects.all()
        
#     if request.method == 'POST':
#         form = RecommendationForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('success')
#     else:
#         form = RecommendationForm()
    
#     return render(request, 'RecQuestion.html', {'quizzes': quizzes})

# def quizQuestion(request, questionID):
#     question = recQuestions.objects.get(pk=questionID)
#     answers = recAnswer.objects.filter(question=question)
#     return render(request, 'MCEQuiz/RecQuestion.html', {'question': question, 'answers': answers})

# def submitAnswer(request):
#     if request.method == 'POST':
#         pass
 
# def showRecommendation(request):
#     pass

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



# #MCE Feedback
def provideFeedback(request):
    submitted = False
    if request.method == "POST":
        form = FeedbackForm(request.POST)
        if form.is_valid():
            form.save()
            #Redirect user back to feedback page. --look into how to output feedback
           # return HttpResponseRedirect('/provideFeedback?submitted=True')
            return redirect('success')
    else:

        form = FeedbackForm()
        if 'submitted' in request.GET:
            submitted = True
            
    #return render(request, 'provideFeedback.html', {'form':form, 'submitted':submitted})
    return render(request, 'pages/provideFeedback.html', {'form':form, 'submitted':submitted})
    

