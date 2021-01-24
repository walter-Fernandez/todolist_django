# TO DO LIST BY WALTER

from django.shortcuts import render, redirect
from .models import *

from .forms import *

# Create your views here.


def index(request):

    task = Task.objects.all()
    form = TaskForm()
#saving  task for our list
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
           form.save()
        return redirect("/")


    context = {'task':task, 'form':form}
    return render(request,'tasks/task.html',context)

#editing our task in our list
def editTask(request,pk):
    task = Task.objects.get(id=pk)
    form = TaskForm(instance=task)

    if request.method =="POST":
        form=TaskForm(request.POST, instance=task)
        if form.is_valid():
           form.save()
        return redirect("/")

    context = {'task':task, 'form':form}
    return render(request,'tasks/edit.html',context)

#deleting our task in our list
def deleteTask(request,pk):
    task= Task.objects.get(id=pk)

    context = {'task': task}

    if request.method == 'POST':
        task.delete()
        return redirect("/")


    return render(request,'tasks/delete.html',context)
