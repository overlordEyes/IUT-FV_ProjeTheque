
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
    # ... URL de Stage...
    path('creer-stage', creer_stage, name='creer-stage'),
    path('stage/modifier/<int:stage_id>/', modifier_stage, name='modifier-stage'),
    path('stage/supprimer/<int:stage_id>/', supprimer_stage, name='supprimer-stage'),
    path('stage/details/<int:stage_id>/', details_stage, name='details-stage'),

    
    #path('', include('stage.urls')),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
