from django.forms import ModelForm
from .models import Topic 
from .models import Entry
from django.forms import Textarea
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class TopicForm(ModelForm):
    class Meta:
        model = Topic 
        fields = ['text']
        labels = {'text': '' }
        
class EntryForm(ModelForm):
    
    class Meta:
     model = Entry
     fields = ['text']     
     labels = {'text': ''}
     widgets = {'text': Textarea(attrs={'cols': 80})}
     
     
class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False, help_text='Optional')
    last_name = forms.CharField(max_length=30, required=False, help_text='Optional')
    email = forms.EmailField(max_length=254, help_text='Enter a valid email address')

    class Meta:
        model = User
        fields = [
            'username', 
            'first_name', 
            'last_name', 
            'email', 
            'password1', 
            'password2', 
            ]     
        
    
        
        