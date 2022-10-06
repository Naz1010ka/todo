from django.shortcuts import render, HttpResponse

def dom(request):
    return render(request, "indexs.html")

def test3(request):
    return render(request, "tests.html")

