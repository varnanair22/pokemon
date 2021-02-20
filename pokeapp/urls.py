from django.urls import path, include
from . import views


urlpatterns = [
path('add_pokemon', views.add_pokemon, name="add_pokemon"),
path('', views.get_pokemon, name="get_pokemon"),
]