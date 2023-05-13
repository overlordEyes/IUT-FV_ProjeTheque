from django.urls import path
from .views import ajouter_stage, stage_detail, liste_stages

urlpatterns = [
    path('stage/ajouter/', ajouter_stage, name='ajouter_stage'),
    path('stage/<int:pk>/', stage_detail, name='stage_detail'),
    path('stages/', liste_stages, name='liste_stages'),
]
