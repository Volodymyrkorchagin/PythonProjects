from django.http import HttpResponse
from datetime import datetime

def table(request):
    result = ""

    for i in range(1, 11):
        for j in range(1, 11):
            result += f"{i} × {j} = {i*j}<br>"

        result += "<hr>"

    return HttpResponse(result)