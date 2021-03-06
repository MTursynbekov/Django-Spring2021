from django.shortcuts import render

# Create your views here.
from .models import TODOList, Task


def todo_list(request, pk):
    todo = TODOList.objects.get(id=pk)
    tasks = Task.objects.filter(todo_list=todo, completed=False)
    context = {"todo": todo, "tasks": tasks, "completed": False, "status": 1}
    return render(request, 'todo_list.html', context=context)


def completed_todo_list(request, pk):
    todo = TODOList.objects.get(id=pk)
    tasks = Task.objects.filter(todo_list=todo, completed=True)
    context = {"todo": todo, "tasks": tasks, "completed": True, "status": 2}
    return render(request, 'completed_todo_list.html', context=context)



