from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.password_validation import validate_password
from .models import CustomUser
from django import forms
from django.contrib.auth.forms import AuthenticationForm


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
    photo_profil = forms.ImageField(required=True, widget=forms.ClearableFileInput(attrs={'accept': 'image/*', 'max-file-size': '5242880'}), label='Photo de profil')


    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = UserCreationForm.Meta.fields + ('type_utilisateur', 'department', 'level', 'cursus', 'role', 'newsletter_subscription', 'nom', 'email', 'password1', 'password2','photo_profil')

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
