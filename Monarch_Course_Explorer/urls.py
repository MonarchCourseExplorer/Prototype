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
from django.urls import path
from Monarch_Course_Explorer import views

urlpatterns = [
    path('', views.homeView, name='home'),
    path('admin/', admin.site.urls),
    path('pages/gallery.html', views.galleryView, name='gallery'),
    path('pages/portfolio.html', views.portfolioView, name='portfolio'),
    path('pages/full-width.html', views.fullWidthView, name='full width'),
    path('pages/sidebar-left.html', views.sidebarLeftView, name='left side bar'),
]
