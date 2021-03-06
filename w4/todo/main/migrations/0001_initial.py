# Generated by Django 3.1.7 on 2021-03-06 00:19

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='TODOList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Название списка')),
            ],
            options={
                'verbose_name': 'Список задач',
                'verbose_name_plural': 'Списки задач',
            },
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300, verbose_name='Название задачи')),
                ('created', models.DateField(auto_now_add=True, verbose_name='Когда создана задача?')),
                ('due', models.DateField(verbose_name='Дедлайн задачи')),
                ('completed', models.BooleanField(default=False, verbose_name='Задача выполнена?')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Автор задачи')),
                ('todo_list', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='main.todolist', verbose_name='К какому списку относиться задача?')),
            ],
            options={
                'verbose_name': 'Задача',
                'verbose_name_plural': 'Задачи',
            },
        ),
    ]
