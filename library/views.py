from django.http import HttpResponse

def home(request):
    return HttpResponse("Головна сторінка")

def writers(request):
    return HttpResponse("Письменники")

def books(request):
    return HttpResponse("Топ книг")