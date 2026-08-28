from django.contrib import admin
from .models import Task, TaskContent

class TaskContentInline(admin.TabularInline):
    model = TaskContent
    extra = 0

class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'date', 'author')
    inlines = [TaskContentInline]


admin.site.register(Task, TaskAdmin)
admin.site.register(TaskContent)