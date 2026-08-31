from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import Task, CustomUser



class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'date', 'author')

class CustomUserAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets + (
    ('Additional Info', {'fields': ('photo',)}),
    )


admin.site.register(Task, TaskAdmin)
admin.site.register(CustomUser, CustomUserAdmin)