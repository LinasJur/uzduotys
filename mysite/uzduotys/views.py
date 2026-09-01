from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic
from .models import Task
from .forms import  UserChangeForm, CustomUserCreateForm

class TaskListView(generic.ListView):
    model = Task
    template_name = 'tasks.html'
    context_object_name = 'tasks'

class TaskDetailView(generic.DetailView):
    model = Task
    template_name = 'task.html'
    context_object_name = 'task'

class UserTaskListView(LoginRequiredMixin, generic.ListView):
    model = Task
    template_name = 'user_tasks.html'
    context_object_name = 'tasks'

    def get_queryset(self):
        return Task.objects.filter(author=self.request.user)

class SignUpView(generic.CreateView):
    form_class = CustomUserCreateForm
    template_name = "signup.html"
    success_url = reverse_lazy("login")

def index(request):

    return render(request, template_name='index.html')

class ProfileUpdateView(LoginRequiredMixin, generic.UpdateView):
    form_class = UserChangeForm
    template_name = "profile.html"
    success_url = reverse_lazy('profile')

    def get_object(self, queryset=None):
        return self.request.user
