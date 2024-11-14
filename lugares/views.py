from django.shortcuts import render
from .models import Lugar

def lugares_disponibles(request):
    lugares = Lugar.objects.filter(estado=Lugar.DISPONIBLE)
    return render(request, 'lugares/lugares_disponibles.html', {'lugares': lugares})

