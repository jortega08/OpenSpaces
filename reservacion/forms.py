from django import forms
from .models import Reserva
from django.forms import DateInput, TimeInput

class ReservaForm(forms.ModelForm):
    class Meta:
        model = Reserva
        fields = ['lugar', 'fecha', 'hora_inicio', 'hora_fin']

    fecha = forms.DateField(widget=DateInput(attrs={'type': 'date'}))
    hora_inicio = forms.TimeField(widget=TimeInput(attrs={'type': 'time'}))
    hora_fin = forms.TimeField(widget=TimeInput(attrs={'type': 'time'}))

