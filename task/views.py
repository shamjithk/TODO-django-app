from django.forms.forms import Form
import task
from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import *
from .forms import *
# Create your views here.

def index(request):
    tasks = Task.objects.all()
    form = TaskForm()
    context = {'tasks':tasks, 'form':form}
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')
    return render(request,'task/list.html',context)

def update(request,id):
    task = Task.objects.get(id=id)
    form = TaskForm(instance=task)
    context = {'form':form}
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
        return redirect('/')
    return render(request,'task/update_task.html',context)

def delete(request,id):
    task = Task.objects.get(id=id)
    context = {'task':task}
    if request.method == "POST":
        task.delete()
        return redirect('/')
    return render(request,'task/delete.html',context)