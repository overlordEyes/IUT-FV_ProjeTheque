from django.db import models
from utilisateur.models import CustomUser
from django.contrib.auth import get_user_model
class Stage(models.Model):
    entreprise = models.CharField(max_length=255)
    raison_sociale = models.CharField(max_length=255)
    contact_email = models.EmailField(max_length=255)
    contact_telephone = models.CharField(max_length=20)
    attestation_fin_stage = models.FileField(upload_to='attestations/', null=True, blank=True)
    etudiant = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
        limit_choices_to={'type_utilisateur': 'et'},
        related_name='stages_etudiant'
    )

    # Référence à un CustomUser avec type_utilisateur="ad" pour administrateur
    encadreur = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
        limit_choices_to={'type_utilisateur': 'ad'},
        related_name='stages_encadreur',
        default=1
        
    )
    rapport_stage = models.FileField(upload_to='rapports/', null=True, blank=True)
    latitude = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)
    longitude = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)
    nombre_stagiaires = models.PositiveIntegerField(null=True, blank=True)
    date_stage = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.entreprise
