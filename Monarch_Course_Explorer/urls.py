# """
# URL configuration for Monarch_Course_Explorer project.
# """

from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from Monarch_Course_Explorer import views

urlpatterns = [
    path('', views.homeView),
    path('index.html', views.homeView, name='home'),
    path('admin/', admin.site.urls),
    path('pages/gallery.html', views.galleryView, name='gallery'),
    path('pages/RecQuestion.html', views.quizView, name='quiz'),
    path('pages/provideFeedback.html', views.provideFeedbackView, name='provideFeedback'),
    path('pages/browseFeedback.html', views.provideBrowseFeedbackView, name='browseFeedback'),
    path('pages/grades.html', views.provideGradesView, name='grades'),
    path('pages/syllabus.html', views.provideSyllabusView, name='syllabus'),
    path('pages/searchResults.html', views.searchResultsView, name='searchResults'),
    path('pages/viewSection.html', views.sectionView, name='viewSection'),
    path('users/', include('django.contrib.auth.urls')) ,
    path('users/', include('users.urls')),
    path('users/templates/authenticate/register.html', views.provideRegisterView, name='registerView'),
    path('users/templates/authenticate/login.html', views.provideStudentLoginView, name='studentLogin'),
    path('users/templates/authenticate/faculty_login.html', views.provideFacultyLoginView, name='facultyLogin'),
    path('catalogue/', include('catalogue.urls'))

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)