from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission
import uuid
def generate_filename(instance, filename):
    extension = filename.split('.')[-1]  # Récupère l'extension du fichier
    unique_filename = f'{uuid.uuid4()}.{extension}'  # Génère un nom unique avec l'extension
    return f'media/photos_profil/{unique_filename}'
class CustomUser(AbstractUser):
    # Champs supplémentaires pour l'utilisateur
    DEPARTMENT_CHOICES = (
        ('dept1', 'Département 1'),
        ('dept2', 'Département 2'),
        # Ajoutez ici les autres choix de département
    )
    LEVEL_CHOICES = (
        ('level1', 'Niveau 1'),
        ('level2', 'Niveau 2'),
        ('level3', 'Niveau 3'),
    )
    CURSUS_CHOICES = (
        ('cursus1', 'Cursus 1'),
        ('cursus2', 'Cursus 2'),
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
    photo_profil = models.ImageField(upload_to=generate_filename, null=True, blank=True, verbose_name='Photo de profil')

    # Champs spécifiques pour l'administration
    ROLE_CHOICES = (
        ('chef_dept', 'Chef de département'),
        ('responsable', 'Responsable'),
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
    
    def __str__(self):
        return self.username
