from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile

class UsrUpdate(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username']
        
class ProfUpdate(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['prof_pic']
        
        
        
        
        
