from django import forms
from django.forms import ModelForm
from .models import *

class AlbumForm(ModelForm):
    class Meta:
        model = Album
        fields = [
            'idAlbum',
            'title',
            'artista',
            'recomendacion',
            'genero',
            'analisis',
            'image'
        ]
        labels = {
            'idAlbum':'ID',
            'title':'Título',
            'artista':'Artista',
            'recomendacion':'Recomendacion',
            'genero':'Genero',
            'analisis':'Analisis',
            'image':'Imagen'
        }
        widgets = {
            'idAlbum':forms.TextInput(attrs={'class':'form-control'}),
            'title':forms.TextInput(attrs={'class':'form-control'}),
            'artista':forms.TextInput(attrs={'class':'form-control'}),
            'recomendacion':forms.Select(attrs={'class':'form-control'}),
            'genero':forms.Select(attrs={'class':'form-control'}),
            'analisis':forms.TextInput(attrs={'class':'form-control'}),
            'image':forms.FileInput(attrs={'class':'form-control'})
        }

class ContactoForm(ModelForm):
    class Meta:
        model = Contactos
        fields = [
            'nombre',
            'apellidoPaterno',
            'apellidoMaterno',
            'correo',
            'comentarios'
        ]
        labels = {
            'nombre':'Nombre',
            'apellidoPaterno':'Apellido Paterno',
            'apellidoMaterno':'Apellido Materno',
            'correo':'Correo Electronico',
            'comentarios':'Comentarios'
        }
        widgets = {
            'nombre':forms.TextInput(attrs={'class':'form-control','id':'nombre','name':'nombre','onblur':'validarNombre()'}),
            'apellidoPaterno':forms.TextInput(attrs={'class':'form-control','id':'appaterno','name':'appaterno','onblur':'validarApellidoP()'}),
            'apellidoMaterno':forms.TextInput(attrs={'class':'form-control','id':'apmaterno','name':'apmaterno','onblur':'validarApellidoM()'}),
            'correo':forms.TextInput(attrs={'class':'form-control','id':'correo','name':'correo','onblur':'validarCorreo()'}),
            'comentarios':forms.Textarea(attrs={'class':'form-control','id':'comentarios','name':'comentarios','placeholder':'Ingrese sus comentarios','rows':'3','onblur':'validarComentarios()'})
        }