from django.shortcuts import redirect, render, HttpResponse
from home.models import Task,threads

# Create your views here.
# def home(request):
#     allthread = threads.objects.all()
#     # for i in allthread:
#     #     tile = Task.objects.filter(thread=i)
#     #print(allthread)
#     if request.method == "POST":
#         context={'success': True}
#         title = request.POST['title']
#         desc = request.POST['desc']
#         tile = request.POST['tile']
#         ins = Task(taskTitle=title, taskDesc=desc,Title=tile)
#         ins.save()
#     else:
#         context = {'success' : False}
        
#     return render(request, 'index.html',context)

def tasks(request):
    allthread = threads.objects.all()
    datas = {}
    for i in range(allthread.count()):
        tile = Task.objects.filter(thread=allthread[i])
        # print(tile)
        datas[f'{allthread[i].Title}'] = tile 
    
    if request.method == "POST":
        desc = request.POST['desc']
        thread_input = request.POST['thread']
        print(thread_input)
        thread_object = threads.objects.filter(Title = thread_input).first()
        # desc = request.POST.get['desc']
        # tile = request.POST.get['tile']
        # ins = Task(taskTitle=title, taskDesc=desc,Title=tile)
        context= {'success': True,'mydict':datas}
        ins = Task(taskDesc=desc,thread = thread_object)
        ins.save()
    else:
        context = {'mydict':datas}
        
    return render(request, 'tasks.html',context)


def threadsa(request):
    allthread = threads.objects.all()
    datas = {}
    for i in range(allthread.count()):
        tile = Task.objects.filter(thread=allthread[i])
        # print(tile)
        datas[f'{allthread[i].Title}'] = tile 
    
    if request.method == "POST":
        title = request.POST['tile']
        print("slo")
        thread_object = threads.objects.create(Title = title)
        context= {'success': True,'thread':allthread}
        
    context= {'mydict':datas}
    return render(request,'tasks.html',context)    







