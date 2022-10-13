from django.shortcuts import render, HttpResponse, redirect
from .models import TODO

def homepage(request):
    return render(request, "index.html")

def test(request):
    todo_list = TODO.objects.all()
    return render(request, "test.html", {"todo_list": todo_list})

def second(request):
    return HttpResponse("test 2 page")

def add_todo(request):
    form = request.POST
    text = form["todo_text"]
    todo = TODO(test=text)
    todo.save()
    return redirect(test)

    



