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


def update_task(request, pk):
    task = Task.objects.get(id=pk)
    form = TaskForm(instance=task)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('home')
    context = {'form': form, 'task': task}
    return render(request, 'task/update.html', context)


def delete_task(request, pk):
    task = Task.objects.get(id=pk)
    if request.method == 'POST':
        task.delete()
        return redirect('home')
    return render(request, 'task/delete.html', {'task': task})
