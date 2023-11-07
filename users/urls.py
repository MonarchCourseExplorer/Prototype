
from django.urls import path
from .import views
#from Monarch_Course_Explorer import views

urlpatterns = [
    path('test', views.test, name="test"),
    path('login_user/', views.login_user, name = "login"),
    path('logout_user/', views.logout_user, name = "logout"),
    path('register', views.register_user, name= "register" ),
    
]