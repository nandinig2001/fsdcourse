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

class CommentForm(forms.Form):
    body = forms.CharField(widget=forms.Textarea(
        attrs={
            "class": "form-control",
            "placeholder": "Leave a comment!"
        })
    )

class PostForm(forms.Form):
    NAME_CHOICES = (('user', 'user'))
    title = forms.CharField(
        max_length=255,
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "Title"
        })
    )    
    body = forms.CharField(widget=forms.Textarea(
        attrs={
            "class": "form-control",
            "placeholder": "Leave a Post!"
        })
    )