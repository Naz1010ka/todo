from django.shortcuts import render, HttpResponse, redirect
from .models import ToMeet, Habits

def dom(request):
    return render(request, "indexs.html")

def test3(request):
    return render(request, "tests.html")


def meet(request):
    return render(request, "meeting.html")

def meet1(request):
    tomeet_list = ToMeet.objects.all()
    return render(request, "meet1.html", {"tomeet_list": tomeet_list})

def add_tome(request):
    form = request.POST
    persone = form["todo_persone"]
    todo = ToMeet(persone=persone)
    todo.save()
    return redirect(meet1)




def delete_to_meet(request,id):
    todo = ToMeet.objects.get(id=id)
    todo.delete()
    return redirect(meet1)

def mark_to_meet(request,id):
    todo = ToMeet.objects.get(id = id)
    todo.is_favorite = True
    todo.save()
    return redirect(meet1)

def closed_todo(request,id):
     todo = ToMeet.objects.get(id=id)
     todo.is_closed = True
     todo.save()
     return redirect (meet1)


def habits(request):
    habits_list = Habits.objects.all()
    return render(request, "habits.html", {"habits_list": habits_list})

def add_habits(request):
    form = request.POST
    text = form["habits_name"]
    todo = Habits(name=text)
    todo.save()
    return redirect(habits)

def del_habits(request, id):
    todo = Habits.objects.get(id=id)
    todo.delete()
    return redirect(habits)

def mark_habits(request, id):
    todo = Habits.objects.get(id=id)
    habits.important = True
    todo.save()
    return redirect(habits)

