from django.shortcuts import render, redirect
from .forms import PagoForm
from .models import Pago

def pago(request):
    if request.method == 'POST':
        form = PagoForm(request.POST)
        if form.is_valid():
            nombre = form.cleaned_data['nombre']
            correo = form.cleaned_data['correo']
            fecha_vencimiento = form.cleaned_data['fecha_vencimiento']

            Pago.objects.create(
                nombre=nombre,
                correo=correo,
                fecha_vencimiento=fecha_vencimiento,
            )
            return redirect('confirmacion')
    else:
        form = PagoForm()
    return render(request, 'pago.html', {'form': form})

def confirmacion(request):
    return render(request, 'confirmacion.html')
