from django.urls import path
from . import views

urlpatterns = [

    #path('quiz/<int:question_id>/', views.quiz_question, name='quiz_question'),
    #path('submit_answer/', views.submit_answer, name='submit_answer'),
    #path('recommendation/', views.show_recommendation, name='show_recommendation'),
    
    #made changes here
    #path('pages/provideFeedback.html', views.provideFeedback, name='provideFeedback'),
    #path('provideFeedback.html', views.provideFeedback, name='provideFeedback'),
    #path('add_feedback', views.add_feedback, name='add-venu'),
    path('upload/', views.uploadSyllabus, name= 'upload'),
    path('success', views.success, name="success"),
    path('provide_feedback/', views.provideFeedback, name='provide_feedback'),
    

    
]
