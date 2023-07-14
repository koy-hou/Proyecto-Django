# Create your models here.
from django.db import models

# Create your models here.
class Recomendacion(models.Model):
    recomendacion = models.CharField(verbose_name='Recomendacion', max_length=50)
    created_at = models.DateTimeField(verbose_name='Fecha creación', auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name='Fecha actualización', auto_now=True)

    class Meta:
        verbose_name = 'Recomendacion'
        verbose_name_plural = 'Recomendaciones'
        ordering = ['recomendacion']

    def __str__(self) -> str:
        return self.recomendacion
    

class Genero(models.Model):
    genero = models.CharField(verbose_name='Genero', max_length=50)
    created_at = models.DateTimeField(verbose_name='Fecha creación', auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name='Fecha actualización', auto_now=True)

    class Meta:
        verbose_name = 'Genero'
        verbose_name_plural = 'Generos'
        ordering = ['genero']

    def __str__(self) -> str:
        return self.genero


class Album(models.Model):
    idAlbum = models.CharField(primary_key=True,verbose_name='ID',max_length=20)
    title = models.CharField(verbose_name='Titulo',max_length=250)
    artista = models.CharField(verbose_name='Artista',max_length=100)
    recomendacion = models.ForeignKey(Recomendacion,verbose_name='Recomendacion',on_delete=models.CASCADE)
    genero = models.ForeignKey(Genero,verbose_name='Genero', on_delete=models.CASCADE)
    analisis = models.CharField(verbose_name='Analisis',max_length=20000)
    image = models.ImageField(verbose_name='Imagen',upload_to='albums',null=True,blank=True)    
    created_at = models.DateTimeField(verbose_name='Fecha creación', auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name='Fecha actualización', auto_now=True)

    class Meta:
        verbose_name = 'album'
        verbose_name_plural = 'albums'
        ordering = ['title','idAlbum']

    def __str__(self) -> str:
        return self.title

class Contactos(models.Model):
    nombre = models.CharField(verbose_name='Nombre',max_length=15)
    apellidoPaterno = models.CharField(verbose_name='Apellido Paterno',max_length=32)
    apellidoMaterno = models.CharField(verbose_name='Apellido Materno',max_length=32)
    correo = models.CharField(verbose_name='Correo Electronico',max_length=32)
    comentarios = models.CharField(verbose_name='Comentarios',max_length=100)
    creacion = models.DateTimeField(verbose_name='Fecha Mensaje', auto_now_add=True)

    class Meta:
        verbose_name = 'contacto'
        verbose_name_plural = 'contactos'
        ordering = ['creacion','nombre','apellidoPaterno','correo']