# Generated by Django 3.2.7 on 2021-10-24 14:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0009_alter_task_thread'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='taskTitle',
        ),
    ]
