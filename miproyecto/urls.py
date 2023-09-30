from django.contrib import admin
from django.urls import path
from mipago.views import pago, confirmacion

urlpatterns = [
    path('admin/', admin.site.urls),
    path('pago/', pago, name='pago'),
    path('confirmacion/', confirmacion, name='confirmacion'),
]
