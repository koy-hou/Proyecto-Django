from django.shortcuts import render, redirect,HttpResponse
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view

from crud.models import *
from .serializers import *

from django.http.response import JsonResponse

@api_view(['GET','POST','DELETE'])

def albums_list(request):
    if request.method == 'GET':
        albums = Album.objects.all()
        
        titulo = request.query_params.get('titulo',None)
        if titulo is not None:
            albums = albums.filter(titulo__contains=titulo)

        artista = request.query_params.get('artista',None)
        if artista is not None:
            albums = albums.filter(artista__contains=artista)

        albums_serializer = AlbumSerializer(albums,many=True)
        return Response(albums_serializer.data)       

    
    elif request.method == 'POST':
        album_data = JSONParser().parse(request)
        album_serializer = AlbumSerializer(data=album_data)
        if album_serializer.is_valid():
            album_serializer.save()
            return JsonResponse(album_serializer.data,status=status.HTTP_201_CREATED)
        else:
            return Response(album_serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        cantidad = Album.objects.all().delete()
        return Response({'mensajes':'Se han eliminado {} albums de la base de datos'.format(cantidad[0])},status=status.HTTP_204_NO_CONTENT)

@api_view(['GET','PUT','DELETE'])
def album_detail(request,album_id):
    try:
        album = Album.objects.get(idAlbum=album_id)
    except:
        return Response({'mensaje':'El album {} no existen en nuestros registros'.format(album_id)},status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        album_serializer = AlbumSerializer(album)
        return Response(album_serializer.data)

    elif request.method == 'PUT':
        album_data = JSONParser().parse(request)
        album_serializer = AlbumSerializer(album, data=album_data)
        if album_serializer.is_valid():
            album_serializer.save()
            return JsonResponse(album_serializer.data,status=status.HTTP_202_ACCEPTED)
        else:
            return Response(album_serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        album.delete()
        return Response({'mensaje':'El album {} ha sido eliminado de la base de datos.'.format(album_id)},status=status.HTTP_204_NO_CONTENT)


@api_view(['GET','POST'])
def reviews_list(request):
    if request.method == 'GET':
        recomendaciones = Recomendacion.objects.all()
        recomendaciones_serializer = RecomendacionSerializer(recomendaciones,many=True)
        return Response(recomendaciones_serializer.data)

    elif request.method == 'POST':
        recomendacion_data = JSONParser().parse(request)
        recomendacion_serializer = recomendacion_serializer(data=recomendacion_data)
        if recomendacion_serializer.is_valid():
            recomendacion_serializer.save()
            return JsonResponse(recomendacion_serializer.data,status=status.HTTP_201_CREATED)
        else:
            return Response(recomendacion_serializer.errors,status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET','PUT','DELETE'])
def review_detail(request,review_id):
    try:
        recomendacion = Recomendacion.objects.get(id=review_id)
    except:
        return Response({'mensaje':'La recomendacion {} no existen en nuestros registros'.format(review_id)},status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        recomendacion_serializer = RecomendacionSerializer(recomendacion)
        return Response(recomendacion_serializer.data)

    elif request.method == 'PUT':
        recomendacion_data = JSONParser().parse(request)
        recomendacion_serializer = recomendacion_serializer(recomendacion, data=recomendacion_data)
        if recomendacion_serializer.is_valid():
            recomendacion_serializer.save()
            return JsonResponse(recomendacion_serializer.data,status=status.HTTP_202_ACCEPTED)
        else:
            return Response(recomendacion_serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        recomendacion.delete()
        return Response({'mensaje':'La recomendación {} ha sido eliminada de la base de datos.'.format(review_id)},status=status.HTTP_204_NO_CONTENT)
