from django.http import HttpResponse
from django.shortcuts import redirect

def home(request):
    return HttpResponse("Головна сторінка")

def writers(request):
    return HttpResponse("Письменники")

def books(request):
    return HttpResponse("Топ книг")


writers_data = {
    "Hemingway": "Ернест Гемінґвей — американський письменник, лауреат Нобелівської премії.",
    "Shakespeare": "Вільям Шекспір — англійський драматург і поет.",
}

books_data = {
    "Harry Potter and the philosopher's stone ": "Перша книга по Гаррі Поттеру.",
    "Harry Potter and the chamber of secrets": "Друга книга по Гаррі Поттеру.",
}

def writer_detail(request, name):
    info = writers_data.get(name)

    if info:
        return HttpResponse(info)
    else:
        return redirect('writers')

def books_detail(request, title):
    info = books_data .get(title)

    if info:
        return HttpResponse(info)
    else:
        return redirect('books')