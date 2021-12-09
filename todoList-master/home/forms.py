from django.forms import ModelForm
from .models import Task,threads

class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = '__all__'
