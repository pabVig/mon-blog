from django.urls import path
from blog import views  # Importer les vues de l'application blog
from django.contrib import admin
from django.contrib.staticfiles.urls import static
from django.urls import path, include
from django.conf import settings
from blog.views import about

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blog.urls')),
    path('about',about,name='about'),
     
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
