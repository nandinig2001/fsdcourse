from django.contrib import admin
from django.urls import path
from django.conf import settings
from . import views
urlpatterns = [
    path('home', views.index, name='home'),
    path('register',views.registerPage,name='register'),
    path('login',views.loginPage,name='login'),
    path('logout',views.logoutPage,name='logout'),
    path('quiz/<str:topicid>',views.quizPage,name='quiz'),
    path('aboutus',views.aboutPage,name='aboutus'),
    path('assignment',views.assignment,name='assignment'),
    path('agnlanding',views.agnlanding,name='agnlanding'),
    path('',views.coverPage,name='cover'),
    path('profile',views.profile,name='profile'),
    path('result',views.quizPage,name='result'),
    path('quiztopic',views.quiztopic,name='quiztopic'),
    path('problemstatement/<str:topicid>',views.problemstatement,name='problemstatement'),
    path('video/<str:topicName>/<str:videoid>', views.video, name='video'),
    path('practice',views.practice,name='practice'),
    path('library',views.library,name='library'),
    path("forum", views.forum, name="forum"),
     path("<str:title>/<str:created_on>", views.forum_detail, name="forum_detail"),
     path("forum_post", views.forum_post, name="forum_post"),
]
