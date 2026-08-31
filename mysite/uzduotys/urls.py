from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.TaskListView.as_view(), name='tasks'),
    path('tasks/<int:pk>/', views.TaskDetailView.as_view(), name='task'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('usertasks/', views.UserTaskListView.as_view(), name='user_tasks'),
    path('signup/', views.SignUpView.as_view(), name='signup'),
]
