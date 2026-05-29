from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime

def home(request):
    now = datetime.now()
    return HttpResponse(f"Поточна дата і час: {now}")

