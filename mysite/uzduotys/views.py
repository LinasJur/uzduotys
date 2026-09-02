from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.db.models import Q
from django.shortcuts import render
from django.urls import reverse_lazy, reverse
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
        tasks = Task.objects.filter(author=self.request.user)
        status = self.request.GET.get('status')
        if status:
            tasks = tasks.filter(status=status)
        return tasks

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

class TaskCreateView(LoginRequiredMixin, generic.CreateView):
    model = Task
    fields = ['title', 'content']
    template_name = 'task_create.html'
    success_url = reverse_lazy('user_tasks')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class TaskUpdateView(LoginRequiredMixin, UserPassesTestMixin, generic.UpdateView, ):
    model = Task
    fields = ['title', 'content', 'status']
    template_name = 'task_create.html'

    def get_success_url(self):
        return reverse('task', kwargs={'pk': self.object.pk})

    def test_func(self):
        return self.get_object().author == self.request.user


class TaskDeleteView(LoginRequiredMixin, UserPassesTestMixin, generic.DeleteView):
    model = Task
    template_name = 'task_delete.html'
    context_object_name = 'task'
    success_url = reverse_lazy('user_tasks')

    def test_func(self):
        return self.get_object().author == self.request.user


def search (request):
    query = request.GET.get('query')
    tasks = Task.objects.filter(
        author=request.user).filter(
        Q(title__icontains=query) |
        Q(content__icontains=query)
    )
    context = {
        'query': query,
        'tasks': tasks
    }
    return render(request, template_name='search.html', context=context)