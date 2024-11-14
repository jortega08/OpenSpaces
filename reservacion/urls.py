from django.urls import path
from . import views

urlpatterns = [
    path('reservar/', views.hacer_reserva, name='reservar'), 
    path('mis_reservas/', views.mis_reservas, name='mis_reservas'), 
    path('editar_reserva/<int:reserva_id>/', views.editar_reserva, name='editar_reserva'),
    path('eliminar_reserva/<int:reserva_id>/', views.eliminar_reserva, name='eliminar_reserva'),
]