from django.shortcuts import render


def db():
    tasks = []
    for i in range(5):
        if i % 2:
            tasks.append(
                {
                    "name": "Task {}".format(i),
                    "created": "10/09/2018",
                    "due": "12/09/2018",
                    "owner": "admin",
                    "mark": "Done"
                }
            )
        else:
            tasks.append(
                {
                    "name": "Task {}".format(i),
                    "created": "10/09/2018",
                    "due": "12/09/2018",
                    "owner": "admin",
                    "mark": "Not Done"
                }
            )

    return tasks


def todo_list(request):
    tasks = db()
    tasks = [task for task in tasks if task["mark"] == "Done"]
    return render(request, 'todo_list.html', context={"tasks": tasks, "status": 1})


def completed_todo_list(request):
    tasks = db()
    tasks = [task for task in tasks if task["mark"] == "Not Done"]
    return render(request, 'completed_todo_list.html', context={"tasks": tasks, "status": 2})
