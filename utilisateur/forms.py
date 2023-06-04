from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.password_validation import validate_password
from .models import CustomUser, Stage
from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.gis.forms import PointField


class GPSButtonWidget(forms.Widget):
    template_name = 'gps_button_widget.html'  # Chemin vers le template HTML du bouton GPS

    def get_context(self, name, value, attrs):
        context = super().get_context(name, value, attrs)
        context['widget']['button_id'] = f"{attrs['id']}_button"  # ID du bouton GPS
        return context

class StageForm(forms.ModelForm):
    encadreurs = forms.ModelChoiceField(
        queryset=CustomUser.objects.filter(role='enca'),
        empty_label='Sélectionnez un encadreur',
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    latitude = forms.FloatField(widget=forms.HiddenInput(), required=False)
    longitude = forms.FloatField(widget=forms.HiddenInput(), required=False)

    class Meta:
        model = Stage
        fields = [
            'entreprise',
            'raison_sociale',
            'contact_email',
            'contact_telephone',
            #'encadreur',
            'attestation_fin_stage',
            'rapport_stage',
            'latitude',
            'longitude',
            'nombre_stagiaires',
            'date_stage',
        ]
        labels = {
            'entreprise': 'Entreprise',
            'raison_sociale': 'Raison sociale',
            'contact_email': 'Adresse email de contact',
            'contact_telephone': 'Numéro de téléphone de contact',
            #'encadreur': 'Encadreur Académique',
            'attestation_fin_stage': 'Attestation de fin de stage',
            'rapport_stage': 'Rapport de stage',
            
            'nombre_stagiaires': 'Nombre de stagiaires',
            'date_stage': 'Date de stage',
        }
        widgets = {
            'entreprise': forms.TextInput(attrs={'class': 'form-control'}),
            'raison_sociale': forms.TextInput(attrs={'class': 'form-control'}),
            'contact_email': forms.EmailInput(attrs={'class': 'form-control'}),
            'contact_telephone': forms.TextInput(attrs={'class': 'form-control'}),
            'attestation_fin_stage': forms.FileInput(attrs={'class': 'form-control-file'}),
            'rapport_stage': forms.FileInput(attrs={'class': 'form-control-file'}),
            'nombre_stagiaires': forms.NumberInput(attrs={'class': 'form-control'}),
            'date_stage': forms.SelectDateWidget(attrs={'class': 'form-control datepicker', 'placeholder': 'YYYY-MM-DD'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['date_stage'].required = True
        encadreur_choices = [
            (encadreur.id, f"{encadreur}_{encadreur.department}")
            for encadreur in CustomUser.objects.filter(role='enca')
        ]
        self.fields['encadreurs'].choices = encadreur_choices
        if self.instance and self.instance.cood_gps:
            self.initial['latitude'] = self.instance.cood_gps.y
            self.initial['longitude'] = self.instance.cood_gps.x

    
        

class CustomUserCreationForm(UserCreationForm):
    username = forms.CharField(max_length=255, widget=forms.TextInput(attrs={'class': 'form-control'}))
    type_utilisateur = forms.ChoiceField(choices=CustomUser.TYPE_CHOICES, widget=forms.Select(attrs={'class': 'form-select'}))
    department = forms.ChoiceField(choices=CustomUser.DEPARTMENT_CHOICES, widget=forms.Select(attrs={'class': 'form-select'}))
    level = forms.ChoiceField(choices=CustomUser.LEVEL_CHOICES, widget=forms.Select(attrs={'class': 'form-select'}))
    cursus = forms.ChoiceField(choices=CustomUser.CURSUS_CHOICES, widget=forms.Select(attrs={'class': 'form-select'}))
    role = forms.ChoiceField(choices=CustomUser.ROLE_CHOICES, widget=forms.Select(attrs={'class': 'form-select'}))
    newsletter_subscription = forms.BooleanField(required=False, widget=forms.CheckboxInput(attrs={'class': 'form-check-input'}))
    nom = forms.CharField(max_length=255, widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(max_length=255, widget=forms.EmailInput(attrs={'class': 'form-control'}))
    password1 = forms.CharField(label='Mot de passe', strip=False, widget=forms.PasswordInput(attrs={'autocomplete': 'new-password', 'class': 'form-control'}), validators=[validate_password])
    password2 = forms.CharField(label='Confirmer le mot de passe', strip=False, widget=forms.PasswordInput(attrs={'autocomplete': 'new-password', 'class': 'form-control'}))
    photo_profil = forms.ImageField(required=False, widget=forms.ClearableFileInput(attrs={'accept': 'image/*', 'max-file-size': '5242880'}), label='Photo de profil')

    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = UserCreationForm.Meta.fields + ('type_utilisateur', 'department', 'level', 'cursus', 'role', 'newsletter_subscription', 'nom', 'email', 'password1', 'password2', 'photo_profil')

class LoginForm(AuthenticationForm):
    username = forms.CharField(
        label='Username',
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter your username'
        })
    )
    password = forms.CharField(
        label='Password',
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter your password'
        })
    )
