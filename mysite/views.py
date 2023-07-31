from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpRequest
from .models import ToDoList, Item


# Create your views here.

def index(request):
    return render(request, 'home.html')

def create(request):
    
    if request.method == 'POST':
        name = request.POST.get('name')
        if len(name) >= 1:
            t = ToDoList(name=name)
            t.save()
            request.user.todolist.add(t)
            return redirect(f'/list/{str(t.id)}/')
    
    return render(request, 'create.html')

def view(request, id):
    ls = ToDoList.objects.get(id=id)
    if request.method == 'POST':
        print(request.POST)
        if 'add' in request.POST:
            text = request.POST.get('text')
            if len(text) >= 1:
                ls.item_set.create(text=text, complete=False)
        
        for item in ls.item_set.all():
            if f'{item.id}_remove' in request.POST:
                item.delete()
            
        for item in ls.item_set.all():
            checkbox_name = f'{str(item.id)}_check'
            if checkbox_name in request.POST:
                item.complete = True
            else:
                item.complete = False
            item.save()
        return redirect(f'/list/{str(ls.id)}')

            
    return render(request, 'list.html', {'ls': ls})

def choose_list(request):
    user = request.user
    for list in user.todolist.all():
        if f'{list.id}_remove' in request.POST:
            list.delete()
    return render(request, 'view.html')



