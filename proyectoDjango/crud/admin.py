from django.contrib import admin
from .models import *

# Register your models here.
class RecomendacionAdmin(admin.ModelAdmin):
    readonly_fields = ('id','created_at','updated_at')
    list_display = ('id','recomendacion')
    ordering = ['recomendacion']

class GeneroAdmin(admin.ModelAdmin):
    readonly_fields = ('id','created_at','updated_at')
    list_display = ('id','genero')
    ordering = ['genero']

class AlbumAdmin(admin.ModelAdmin):
    readonly_fields = ('created_at','updated_at')
    list_display = ('idAlbum','title','artista','recomendacion','analisis')
    ordering = ['title','artista']

class ContactoAdmin(admin.ModelAdmin):
    readonly_fields = ('creacion','id','nombre','apellidoPaterno','apellidoMaterno','correo','comentarios')
    list_display = ('id','nombre','apellidoPaterno','apellidoMaterno','correo','creacion','comentarios')
    ordering = ['creacion','nombre','apellidoPaterno','correo']



admin.site.register(Recomendacion,RecomendacionAdmin)
admin.site.register(Album,AlbumAdmin)
admin.site.register(Genero,GeneroAdmin)
admin.site.register(Contactos,ContactoAdmin)