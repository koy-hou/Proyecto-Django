from django.urls import path
from .views import *

urlpatterns = [
    path('albums/', albums_list),
    path('albums/<int:album_id>', album_detail),
    path('genero/', genero_list),
    path('genero/<int:album_id>', genero_detail),
    path('recomendaciones/', reviews_list),
    path('recomendaciones/<int:review_id>', review_detail),
]