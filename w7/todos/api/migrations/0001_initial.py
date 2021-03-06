# Generated by Django 3.1.7 on 2021-03-20 03:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300, verbose_name='Название задачи')),
                ('created', models.DateField(auto_now_add=True, verbose_name='Когда создана задача?')),
                ('due_on', models.DateField(verbose_name='Дедлайн задачи')),
                ('completed', models.BooleanField(default=False, verbose_name='Задача выполнена?')),
            ],
            options={
                'verbose_name': 'Задача',
                'verbose_name_plural': 'Задачи',
                'ordering': ['id', 'name'],
            },
        ),
        migrations.CreateModel(
            name='TODOList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Название списка')),
            ],
            options={
                'verbose_name': 'Список задач',
                'verbose_name_plural': 'Списки задач',
                'ordering': ['id', 'name'],
            },
        ),
    ]
