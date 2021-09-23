from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
from .models import *



class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email','password1','password2']

# class addQuestionform(ModelForm):
#     class Meta:
#         model=Quizz
#         fields=('_all_',)
class ProfileUpdateForm(ModelForm):
    class Meta:
        model=Page
        fields=['pfname','plname','pmobile','pcollege','page']
