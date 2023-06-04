from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission
from django.urls import reverse
from datetime import date
from django.contrib.gis.db import models


def get_stage_url(self):
        if self.type_utilisateur == 'et':
            if self.stage:
                return reverse('modifier_stage', args=[self.stage.id])
            else:
                return reverse('creer_stage')
        return ''

from django.contrib.gis.db import models

def generate_filename(instance, filename):
    extension = filename.split('.')[-1]
    unique_filename = f'{uuid.uuid4()}.{extension}'
    return f'media/photos_profil/{unique_filename}'

class Stage(models.Model):
    entreprise = models.CharField(max_length=255)
    raison_sociale = models.CharField(max_length=255)
    contact_email = models.EmailField(max_length=255)
    contact_telephone = models.CharField(max_length=20)
    attestation_fin_stage = models.FileField(upload_to='attestations/', null=True, blank=True)
    cood_gps = models.PointField(null=True, blank=True)  # Ajout des options null=True, blank=True
    rapport_stage = models.FileField(upload_to='rapports/', null=True, blank=True)
    nombre_stagiaires = models.PositiveIntegerField(null=True, blank=True)
    encadreur = models.CharField(max_length=255, blank=False)
    owner = models.CharField(max_length=255, blank=False, default="pas de proprietaire")
    date_stage = models.DateField(null=False, blank=False, default=date.today)

    def __str__(self):
        return self.entreprise

   



class CustomUser(AbstractUser):
    # Champs supplémentaires pour l'utilisateur
    DEPARTMENT_CHOICES = (
        ('GEL', 'Genie Electrique'),
        ('GTE', 'Genie Thermique,Energie et Environnement'),
        ('GTR', 'Genie des Telecommunications et Reseaux'),
        ('GIN', 'Genie informatique'),
        ('GEC', 'Genie Civil'),
        ('GEA', 'Gestion des Entreprises et des Administrations'),
        ('GMP', 'Genie de Mecatronik et productique '),
        ('IBM', 'Ingenierie Biomedical'),
        ('GTI', 'Genie Thermique et Energetique Industriel'),
        # Ajoutez ici les autres choix de département
    )
    LEVEL_CHOICES = (
        ('level1', 'Niveau 1'),
        ('level2', 'Niveau 2'),
        ('level3', 'Niveau 3'),
    )
    CURSUS_CHOICES = (
        ('AII', 'Automatique informatique industrielle et Electronique'),
        ('CGE', 'Comptabilite et gestion des Entreprises'),
        ('MCV', 'Marketing comerce vente'),
        ('BAT', 'Batiment'),
        ('TPU', 'Travaux Publics'),
        ('ELT', 'Electrotechnique'),
        ('MSE', 'Maintenance des Systemes Electronique'),
        ('FCL', 'Froid et Climatisation'),
        ('BQF', 'Banque Finance'),
        ('MEV', 'Management Evenementiel'),
        ('GMH', 'Gestion Management Hotelier'),
        ('CDRI', 'Concepteur Developpeur Reseau internet'),
        ('QSIR', 'Qualite, Securite,Internet et Reseau'),
        ('GGE', 'Genie Geomatique'),
        ('MIP', 'Maintenance industrielle et Productique'),
        ('IRT', 'Ingenierie des Reseaux et telecommunication'),
        ('GMIE', 'Gestion et Maintenance des Installations Energetiques'),
        ('GCF', 'Gestion Comptabilite et Financiere'),
        ('GMO', 'Gestion et Management des Organisations'),
        ('BGA', 'Banque Gestionnaire des Actifs'),
        ('MAN', 'Marketing Numerique'),
        # Ajoutez ici les autres choix de cursus
    )
    TYPE_CHOICES = (
        ('vis', 'visiteur'),
        ('et', 'etudiant'),
        ('ad', 'administration'),
        # Ajoutez ici les autres choix de type d'utilisateur
    )
    
    # Champs spécifiques pour les étudiants
    type_utilisateur = models.CharField(max_length=3, choices=TYPE_CHOICES, null=False, blank=False, default="vis")
    department = models.CharField(max_length=50, choices=DEPARTMENT_CHOICES, null=True, blank=True)
    level = models.CharField(max_length=50, choices=LEVEL_CHOICES, null=True, blank=True)
    cursus = models.CharField(max_length=50, choices=CURSUS_CHOICES, null=True, blank=True)
    photo_profil = models.ImageField(upload_to=generate_filename, null=False, blank=False, verbose_name='Photo de profil', default='media\photos_profil\pp.png')


    # Champs spécifiques pour l'administration
    ROLE_CHOICES = (
        ('chef_dept', 'Chef de département'),
        ('responsable', 'Responsable de niveau'),
        ('enca', 'Encadreur'),
        # Ajoutez ici les autres choix de rôles pour l'administration
    )
    role = models.CharField(max_length=50, choices=ROLE_CHOICES, null=True, blank=True)
    
    # Champs spécifiques pour les visiteurs
    newsletter_subscription = models.BooleanField(default=False)
    
    # Champs spécifiques à votre modèle d'utilisateur
    nom = models.CharField(max_length=255, blank=False, default="nom test")

    # Utilisation d'un related_name personnalisé pour le champ 'groups'
    groups = models.ManyToManyField(Group, verbose_name='user groups', blank=True, related_name='custom_users')
    
    # Utilisation d'un related_name personnalisé pour le champ 'user_permissions'
    user_permissions = models.ManyToManyField(Permission, verbose_name='user permissions', blank=True, related_name='custom_users_permissions')
    
    #Stage
    stage = models.OneToOneField(Stage, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.nom
    
    
    
 