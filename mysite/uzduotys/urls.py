from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('tasks/<int:pk>/', views.TaskDetailView.as_view(), name='task'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('usertasks/', views.UserTaskListView.as_view(), name='user_tasks'),
    path('signup/', views.SignUpView.as_view(), name='signup'),
    path('profile/', views.ProfileUpdateView.as_view(), name='profile'),
    path('tasks/create/', views.TaskCreateView.as_view(), name='task_create' ),
    path('tasks/<int:pk>/update/', views.TaskUpdateView.as_view(), name='task_update' ),


]
