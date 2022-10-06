from django.shortcuts import render, HttpResponse

def dom(request):
    return HttpResponse("Это тест")

def test3(request):
    return render(request, "test.html")

