from django.shortcuts import render, HttpResponse
from .models import ToMeet

def dom(request):
    return render(request, "indexs.html")

def test3(request):
    return render(request, "tests.html")


def meet(request):
    return render(request, "meeting.html")

def meet1(request):
    tomeet_list = ToMeet.objects.all()
    return render(request, "meet1.html", {"tomeet_list": tomeet_list})