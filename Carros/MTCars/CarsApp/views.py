from django.shortcuts import render
from CarsApp.models import MTCars


def searchf(request):
    if request.method == 'GET':
        return render(request, 'CarsApp/home.html')
    else:
        search_query = request.POST.get('search')
        carros = MTCars.objects.filter(name__icontains=search_query)
        contexto = {
            'search_query': search_query,
            'carros': carros
        }
        return render(request, 'CarsApp/home.html', contexto)


def detalhes(request, carro_id):
    carro = MTCars.objects.get(id=carro_id)
    contexto = {
        'carro': carro
    }
    return render(request, 'CarsApp/detalhes.html', contexto)
