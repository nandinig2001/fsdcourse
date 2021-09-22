from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.conf import settings
from django.contrib.auth.models import User
from django.core.mail import send_mail, EmailMessage
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm
from django.contrib.auth import authenticate,login, logout
# Create your views here.
def index(request):
    return render(request,'index.html')

def registerPage(request):
    form = CreateUserForm()
    if request.method=='POST':
        print("Successful")
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request,'Account was created for'+user)

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
            print("Loggeg In")
            return redirect('index')
        else:
          messages.info(request, 'Username OR password is incorrect')
    context = {}
    return render(request,'login.html')

def logoutPage(request):
    logout(request)
    return redirect('login')
