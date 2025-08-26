from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [
    path('', homepage, name='homepage'),
    path('about/', about, name='about'),
    path('bozhena-sadova/', bozhenasadova, name='bozhena-sadova'),
]
