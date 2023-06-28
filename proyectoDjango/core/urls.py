from django.urls import path
from .views import *

urlpatterns = [
    path('', root),
    path('home/', home, name='home'),
    path('album/', album, name='album'),
    path('album/resena/<str:album_id>', album_recomendado, name="album-resena"),
    path('about/', about, name='about'),
    path('contact/', contact, name='contact'),
]