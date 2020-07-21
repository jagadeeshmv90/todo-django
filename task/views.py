from django.shortcuts import render, redirect
from .models import *
from .forms import *


def index(request):
    form = TaskForm()
    tasks = Task.objects.all().order_by('-created')
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    context = {'form': form, 'tasks': tasks}
    return render(request, 'task/index.html', context)
