from django.urls import path
from .views import lugares_disponibles

urlpatterns = [
    path('', lugares_disponibles, name='lugares_disponibles'),
]
