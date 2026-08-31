from django.shortcuts import render
from django.views import generic
from .models import Task, TaskContent

class TaskListView(generic.ListView):
    model = Task
    template_name = 'tasks.html'
    context_object_name = 'tasks'

class TaskDetailView(generic.DetailView):
    model = Task
    template_name = 'task.html'
    context_object_name = 'task'

    
