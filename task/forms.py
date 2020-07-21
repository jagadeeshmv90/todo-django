from django import forms
from django.forms import ModelForm
from .models import *


class TaskForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Enter task name'}))

    class Meta:
        model = Task
        fields = '__all__'
