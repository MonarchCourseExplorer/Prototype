
from django.urls import path
from .import views
#from Monarch_Course_Explorer import views

urlpatterns = [
    path('test', views.test, name="test"),
    path('test2', views.test_two, name="test2"),
    path('test3', views.test_three, name="test3"),
    path('login_user/', views.login_user, name = "login"),
    path('login_faculty_user/', views.login_faculty_user, name = "flogin"),
    path('logout_user/', views.logout_user, name = "logout"),
    path('register', views.register_user, name= "register" ),
    
]