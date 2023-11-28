from django.urls import path
from . import views

urlpatterns = [
    path('quiz/<int:question_id>/', views.quizQuestion, name='quizQuestion'),
    path('submit_answer/', views.submitAnswer, name='submitAnswer'),
    path('recommendation/', views.showRecommendation, name='showRecommendation'),
    path('pages/provideFeedback.html', views.provideFeedback, name='provideFeedback'),
    path('upload/', views.uploadSyllabus, name= 'upload'),
    path('success', views.success, name="success"),
]