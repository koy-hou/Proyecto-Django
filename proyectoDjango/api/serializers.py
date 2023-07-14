from dataclasses import field
from rest_framework import serializers
from crud.models import *


class AlbumSerializer(serializers.ModelSerializer):
    class Meta:
        model = Album
        fields = (
            'idAlbum','title','artista','recomendacion','analisis','created_at','updated_at'
        )

class RecomendacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recomendacion
        fields = (
            'id','recomendacion','created_at','updated_at'
        )

class GenerosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genero
        fields = (
            'id','genero','created_at','updated_at'
        )
