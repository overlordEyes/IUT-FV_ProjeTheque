from django import forms
from .models import Stage

class StageForm(forms.ModelForm):
    class Meta:
        model = Stage
        fields = ['etudiant', 'raison_sociale', 'contact_email', 'contact_telephone', 'attestation_fin_stage', 'encadreur', 'rapport_stage', 'latitude','longitude', 'nombre_stagiaires', 'date_stage']
        labels = {
            'etudiant': 'Étudiant',
            'raison_sociale': 'Nom de l\'entreprise',
            'contact_email': 'Contact Email de l\'entreprise',
            'contact_telephone': 'Contact Téléphone de l\'entreprise',
            'attestation_fin_stage': 'Attestation de fin de stage',
            'encadreur': 'Encadreur',
            'rapport_stage': 'Rapport de stage',
            'longitude': 'longitude GPS',
            'latitude': 'latitude GPS',
            'nombre_stagiaires_recus': 'Nombre de stagiaires reçus',
            'date_stage': 'date de debut du stage',
        }
        widgets = {
            'etudiant': forms.Select(attrs={'class': 'form-select'}),
            'raison_sociale': forms.TextInput(attrs={'class': 'form-control'}),
            'contact_email': forms.EmailInput(attrs={'class': 'form-control'}),
            'contact_telephone': forms.TextInput(attrs={'class': 'form-control'}),
            'attestation_fin_stage': forms.FileInput(attrs={'class': 'form-control'}),
            'encadreur': forms.Select(attrs={'class': 'form-select'}),
            'rapport_stage': forms.FileInput(attrs={'class': 'form-control'}),
            'longitude': forms.TextInput(attrs={'class': 'form-control'}),
            'latitude': forms.TextInput(attrs={'class': 'form-control'}),
            'nombre_stagiaires_recus': forms.NumberInput(attrs={'class': 'form-control'}),
            'date_stage': forms.DateInput(attrs={'class': 'form-control'}),
        }
