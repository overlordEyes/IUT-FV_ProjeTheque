from django.contrib import admin
from .models import CustomUser, Stage

admin.site.register(CustomUser)
from django.contrib import admin

class StageAdmin(admin.ModelAdmin):
    # Liste des champs à afficher dans l'administration
    list_display = ('owner','entreprise', 'raison_sociale', 'contact_email', 'date_stage', 'encadreur', 'cood_gps', 'rapport_stage','attestation_fin_stage')

# Enregistrer le modèle Stage et la classe StageAdmin pour l'administration
admin.site.register(Stage, StageAdmin)