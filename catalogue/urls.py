from django.urls import path
from . import views

urlpatterns = [
    path('upload/', views.uploadSyllabus, name= 'upload'),
    path('success', views.success, name="success"),
    path('syllabusSuccess', views.syllabusSuccess, name="syllabusSuccess"),
    path('provide_feedback/', views.provideFeedback, name='provide_feedback'),
]