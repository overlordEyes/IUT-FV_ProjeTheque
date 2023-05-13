
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from utilisateur.views import *
urlpatterns = [
    # Autres URLs de votre projet
    path('admin/', admin.site.urls),
    path('', connexion, name='accueil'),  # Ajoutez cette ligne pour l'URL racine
    path('profile/', profile, name='profile'),
    path('edit_profile/', edit_profil, name='edit_profil'),
    path('inscription/', inscription, name='inscription'),
    path('connexion/', connexion, name='connexion'),
    path('', include('stage.urls')),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
