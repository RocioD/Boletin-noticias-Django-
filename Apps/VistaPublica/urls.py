from django.urls import path, include

from Apps.VistaPublica.views import *

urlpatterns = [
    path('', Index, name="Index"),
    path('detalle/<int:id>/', Detalle, name="Detalle"),
    path('noticias', Noticias, name="Noticias"),
    path('eventos', Eventos, name="Eventos"),
]
