"""Blogman URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from . import views as blog_views

urlpatterns = [
     path('',blog_views.index,name="home"),
     path('about',blog_views.about,name="about"),
     path('blog',blog_views.blog_page, name="blog"),
     path('login',blog_views.login_view,name="login"),
     path('logout',blog_views.logout_user,name="logout"),
     path('profilepage',blog_views.profile,name="profile"),
     path('signup',blog_views.signup, name='signup'),
     path('desc/<int:id>',blog_views.desc, name='desc')
]
