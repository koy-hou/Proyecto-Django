from django.urls import path
from .views import *

urlpatterns = [
    path('', root, name='log'),
    path('login', login, name='login'),
    path('success', success, name='success'),
    path('register/register', registerVal, name='registerVal'),
    path('register/', register, name='register'),
    path('logout', logout, name='logout'),
]