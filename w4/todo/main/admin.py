from django.contrib import admin

# Register your models here.
from .models import TODOList, Task


@admin.register(TODOList)
class TodoAdmin(admin.ModelAdmin):
    list_display = ['name', ]
    ordering = ['name']


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ['name', 'created', 'due_on', 'owner', 'todo_list']
    ordering = ['name']
    search_fields = ['name', 'owner__first_name', 'todo_list__name', ]
    list_filter = ['created', 'due_on', ]
