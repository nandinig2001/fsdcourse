from django.contrib import admin
from django.urls import path
from django.conf import settings
from . import views
urlpatterns = [
    path('home', views.index, name='home'),
    path('register',views.registerPage,name='register'),
    path('login',views.loginPage,name='login'),
    path('logout',views.logoutPage,name='logout'),
    path('quiz',views.quizPage,name='quiz'),
    path('aboutus',views.aboutPage,name='aboutus'),
    path('assignment',views.assignment,name='assignment'),
    path('agnlanding',views.agnlanding,name='agnlanding'),
    path('',views.coverPage,name='cover'), 

]
