from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.conf import settings
from django.contrib.auth.models import User
from django.core.mail import send_mail, EmailMessage
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from .forms import *
from .models import *
from django.contrib.auth import authenticate,login, logout
from datetime import datetime

# Create your views here.
def index(request):
    return render(request,'home.html')

def registerPage(request):
    form = CreateUserForm()
    if request.method=='POST':
        print("Successful")
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request,'Account created for '+user)

            return redirect('login')
    context ={'form':form}
    return render(request,'register.html',context)

def loginPage(request):
    if request.method == 'POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        user = authenticate(request, password=password, username=username)
        if user is not None:
            login(request,user)
            print("Logged In")
            return redirect('home')
        else:
          messages.info(request, 'Incorrect username OR password')
    context = {}
    return render(request,'login.html')

def logoutPage(request):
    logout(request)
    return redirect('cover')

def quizPage(request,topicid):
    if request.method == 'POST':
             

        questions=Quizz.objects.filter(topic=topicid)
        score=0
        wrong=0
        correct=0
        total=0
        for q in questions:
            total+=1
            print(request.POST.get(q.question))
            print(q.ans)
            print()
            if q.ans ==  request.POST.get(q.question):
                score+=10
                correct+=1
            else:
                wrong+=1
        percent = score/(total*10) *100
        context = {
            'score':score,
            'time': request.POST.get('timer'),
            'correct':correct,
            'wrong':wrong,
            'percent':percent,
            'total':total
        }
        return render(request,'result.html',context)
    else:
        questions=Quizz.objects.filter(topic=topicid)
        context = {
            'questions':questions,
            'topicid':topicid
        }
        return render(request,'quiz.html',context)


def aboutPage(request):
    context ={}
    return render(request,'aboutus.html')

def coverPage(request):
    context ={}
    print("success")
    return render(request,'index.html')



def agnlanding(request):
    context ={}
    print("success")
    return render(request,'agnlanding.html')

def assignment(request):
    if request.method == 'POST':

        name = request.POST.get('name', '')
        g1 = request.POST.get('g1', '')
        w1 = request.POST.get('w1', '')
        g2 = request.POST.get('g2', '')
        w2 = request.POST.get('w2','')
        assignment = Assignment( name=name, g1 = g1, w1 = w1, g2 =g2, w2 = w2)
        assignment.save()
        messages.success(request,'Solution Submitted')
    return render(request,'assignment.html')


def profile(request):
    user=request.user
    print(user.page.pfname)
    form = ProfileUpdateForm(request.POST or None,instance=user.page)
    if request.method=='POST':
        print("Successful")

        if form.is_valid():
            form.save()
        # user = form.cleaned_data.get('username')
        # messages.success(request,'Account created for '+user)

            return redirect('profile')
    else:
        
        Pages=Page.objects.filter(user=request.user)
        context={'Pages':Pages}
        return render(request,'profile.html',context)

def quiztopic(request):
    return render(request,'quiztopic.html')


def problemstatement(request,topicid):
    questions= Aquestions.objects.filter(topic=topicid)
    context = {
         'questions':questions
         }
    return render(request,'problemstatement.html',context)


def video(request, topicName,videoid):
    
    head=''
    videos = Video.objects.filter(topic = topicName)
    loadedvideo = Video.objects.filter(topic = topicName , videoid = videoid)
    print(topicName)
    for items in videos:
        head = items.topicName
    count = Video.objects.filter().count()
    
    return render(request,'video.html', context={'videos': videos, 'head': head, 'loadedvideo':loadedvideo, 'topicid':topicName })

def practice(request):
    return render(request,'practice.html')