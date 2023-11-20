from django.urls import path
from . import views

urlpatterns = [
    path('quiz/<int:question_id>/', views.quiz_question, name='quiz_question'),
    path('submit_answer/', views.submit_answer, name='submit_answer'),
    path('recommendation/', views.show_recommendation, name='show_recommendation'),
    path('pages/provideFeedback.html', views.provideFeedbackView, name='provideFeedback'),
]