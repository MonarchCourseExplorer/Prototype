"""
URL configuration for Monarch_Course_Explorer project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from Monarch_Course_Explorer import views

urlpatterns = [
    path('', views.homeView),
    path('index.html', views.homeView, name='home'),
    path('admin/', admin.site.urls),
    path('pages/gallery.html', views.galleryView, name='gallery'),
    path('catalogue/templates/MCEQuiz/RecQuestion.html', views.quizView, name='quiz'),
    path('pages/provideFeedback.html', views.provideFeedbackView, name='provideFeedback'),
    path('pages/browseFeedback.html', views.provideBrowseFeedbackView, name='browseFeedback'),
    path('pages/grades.html', views.provideGradesView, name='grades'),
    path('pages/syllabus.html', views.provideSyllabusView, name='syllabus'),
    path('users/', include('django.contrib.auth.urls')) ,
    path('users/', include('users.urls')) 
]
