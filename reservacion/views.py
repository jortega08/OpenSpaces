from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .forms import ReservaForm
from .models import Reserva
from lugares.models import Lugar, TipoLugar

# Vista para hacer una reserva
def hacer_reserva(request):
    if request.method == 'POST':
        form = ReservaForm(request.POST)
        if form.is_valid():
            reserva = form.save(commit=False)  # No guardamos aún
            reserva.usuario = request.user  # Asignamos el usuario actual
            reserva.save()  # Ahora sí guardamos
            return redirect('mis_reservas')  # Redirige a la página de "Mis Reservas" después de guardar
    else:
        form = ReservaForm()

    return render(request, 'reservas/reservar.html', {'form': form})

# Vista para ver las reservas del usuario
def mis_reservas(request):
    reservas = Reserva.objects.filter(usuario=request.user)  # Filtrar por el usuario actual
    return render(request, 'reservas/mis_reservas.html', {'reservas': reservas})

# Vista para eliminar una reserva
def eliminar_reserva(request, reserva_id):
    reserva = get_object_or_404(Reserva, id=reserva_id)
    reserva.delete()  # Eliminar la reserva
    return redirect('mis_reservas')  # Redirigir a la página de Mis Reservas después de eliminar

# Vista para editar una reserva existente
def editar_reserva(request, reserva_id):
    reserva = get_object_or_404(Reserva, id=reserva_id)

    if request.method == 'POST':
        form = ReservaForm(request.POST, instance=reserva)
        if form.is_valid():
            form.save()
            return redirect('mis_reservas')  # Redirigir a la página de Mis Reservas después de guardar
    else:
        form = ReservaForm(instance=reserva)

    return render(request, 'reservas/editar_reserva.html', {'reserva': reserva, 'form': form})

# Vista para renderizar la página de reserva
def reservar(request):
    return render(request, 'reservas/reservar.html')
