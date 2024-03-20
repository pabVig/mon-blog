from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # Définit l'URL racine pour la vue index de l'application blog
    # Ajoutez d'autres URLs si nécessaire
]
