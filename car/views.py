from django.shortcuts import render

def main(request):
    return render(request, 'car/main_page.html', {})

def toyota(request):
    return render(request, 'car/model_of_cars.html', {
        'brand': 'Toyota',
        'country': 'Japan'
    })

def honda(request):
    return render(request, 'car/model_of_cars.html', {
        'brand': 'Honda',
        'country': 'Japan'
    })

def renault(request):
    return render(request, 'car/model_of_cars.html', {
        'brand': 'Renault',
        'country': 'France'
    })