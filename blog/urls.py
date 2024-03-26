from django.urls import path
from . import views  # Assurez-vous d'importer le module views de votre application



urlpatterns = [
    path('', views.index, name='index'),  # URL pour la page d'accueil
    path('about/', views.about, name='about'),
    path('histoire/', views.story, name='histoire'),
    path('galerie/', views.galerie, name='galerie'),
    path('calendrier/', views.calendrier, name='calendrier'),
    # URL pour la page "about.html"
    # Autres URLs...
]

