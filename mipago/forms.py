from django import forms

class PagoForm(forms.Form):
    nombre = forms.CharField(label='Nombre', max_length=100)
    correo = forms.EmailField(label='Correo')
    numero_tarjeta = forms.CharField(label='Número de Tarjeta', max_length=16)
    contrasena_tarjeta = forms.CharField(label='Contraseña de Tarjeta', max_length=4, widget=forms.PasswordInput)
    fecha_vencimiento = forms.DateField(label='Fecha de Vencimiento')
