from django.shortcuts import render, HttpResponse
from home.models import Task,threads

# Create your views here.
def home(request):
    allthread=threads.objects.all()
    for i in allthread:
        tile = Task.objects.filter(thread=i)
    if request.method == "POST":
        context={'success': True}
        title = request.POST['title']
        desc = request.POST['desc']
        tile = request.POST['tile']
        ins = Task(taskTitle=title, taskDesc=desc,Title=tile)
        ins.save()
    else:
        context = {'success' : False}
        
    return render(request, 'index.html',context)

def tasks(request):
    allTasks = Task.objects.all()
    context = {'tasks':allTasks}
    return render(request, 'tasks.html',context)

def thread(request):
    allthread=threads.objects.all()
    context = {'thread':allthread}
    return render(request,'tasks.html',context)    







