from django.urls import path, include

from Apps.AdminNoticias.views import *

urlpatterns = [
    path('', noticias_listar, name="noticias_listar"),
    path('crear/', noticias_crear, name="noticias_crear"),
    path('borrar/<int:id>/', noticias_borrar, name="noticias_borrar"),
    path('editar/<int:id>/', noticias_editar, name="noticias_editar"),
]
