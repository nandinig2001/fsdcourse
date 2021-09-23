from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.conf import settings
from django.contrib.auth.models import User
from django.core.mail import send_mail, EmailMessage
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm
from .models import Assignment,Page
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

def quizPage(request):
    context ={}
    return render(request,'quiz.html')

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
    Pages=Page.objects.filter(user=request.user)
    context={'Pages':Pages}
    return render(request,'profile.html',context)
