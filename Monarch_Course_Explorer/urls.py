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
    path('', views.homeView),
    path('index.html', views.homeView, name='home'),
    path('admin/', admin.site.urls),
    path('pages/gallery.html', views.galleryView, name='gallery'),
    path('pages/portfolio.html', views.portfolioView, name='portfolio'),
    path('pages/full-width.html', views.fullWidthView, name='full-width'),
    path('pages/sidebar-left.html', views.sidebarLeftView, name='sidebar-left'),
    path('pages/sidebar-left-2.html', views.sidebarLeftView2, name='sidebar-left 2'),
    path('pages/sidebar-right.html', views.sidebarRightView, name='sidebar-right'),
    path('pages/sidebar-right-2.html', views.sidebarRightView2, name='sidebar-right 2'),
    path('pages/basic-grid.html', views.basicGridView, name='basic-grid')
]
