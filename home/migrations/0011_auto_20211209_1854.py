# Generated by Django 3.1.7 on 2021-12-09 13:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0010_remove_task_tasktitle'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='taskTitle',
            field=models.CharField(default='NONE', max_length=40, verbose_name='Task Title'),
        ),
        migrations.AlterField(
            model_name='task',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='threads',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]