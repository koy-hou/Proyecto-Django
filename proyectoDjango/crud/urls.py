from django.urls import path
from .views import *

urlpatterns = [
    path('', root),
    path('albums/', album_lista, name="albums"),
    path('albums/nuevo/', album_nuevo, name="album-nuevo"),
    path('album/detalle/<str:album_id>', album_detalle, name="album-detalle"),
    path('album/editar/<str:album_id>', album_editar, name="album-editar"),
    path('album/<str:album_id>/eliminar', album_eliminar, name="album-eliminar"),
]

