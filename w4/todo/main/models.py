from django.conf import settings
from django.db import models


# Create your models here.

class TODOList(models.Model):
    class Meta:
        verbose_name = "Список задач"
        verbose_name_plural = "Списки задач"

    name = models.CharField(max_length=200, verbose_name="Название списка")

    def __str__(self):
        return self.name


class Task(models.Model):
    class Meta:
        verbose_name = "Задача"
        verbose_name_plural = "Задачи"

    name = models.CharField(max_length=300, verbose_name="Название задачи")
    created = models.DateField(auto_now_add=True, verbose_name="Когда создана задача?")
    due_on = models.DateField(verbose_name="Дедлайн задачи")
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name="Автор задачи")
    completed = models.BooleanField(default=False, verbose_name="Задача выполнена?")
    todo_list = models.ForeignKey(TODOList,
                                  on_delete=models.CASCADE,
                                  verbose_name="К какому списку относиться задача?",
                                  null=True)

    def __str__(self):
        return self.name
