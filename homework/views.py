from django.shortcuts import render, HttpResponse
from .models import ToMeet

def dom(request):
    return render(request, "indexs.html")

def test3(request):
    return render(request, "tests.html")


def meet(request):
    return render(request, "meeteng.html", {"todo_list": todo_list})