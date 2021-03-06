from django.urls import path

from .views import todo_list, completed_todo_list

urlpatterns = [
    path(r'todos/<int:pk>/', todo_list),
    path(r'todos/<int:pk>/completed/', completed_todo_list)
]
