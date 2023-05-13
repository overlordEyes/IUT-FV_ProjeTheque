from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth import authenticate
from utilisateur.forms import *

from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login


def inscription(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password1'])

            # Vérifier la valeur du champ type_utilisateur
            if user.type_utilisateur == 'ad':
                user.department = None
                user.level = None
                user.cursus = None
                # Définir les autres champs à NULL

            elif user.type_utilisateur == 'et':
                user.role = None
                # Définir les autres champs à NULL
            elif user.type_utilisateur == 'vis':
                user.department = None
                user.level = None
                user.cursus = None
                user.role = None
            user.save()
            return redirect('connexion')  # Rediriger vers une page de succès
    else:
        form = CustomUserCreationForm()
    
    return render(request, 'inscription.html', {'form': form})


def connexion(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = None
            
            # Check if the username is an email
            if '@' in username:
                try:
                    user = User.objects.get(email=username)
                except User.DoesNotExist:
                    pass
            
            # If the username is not an email or no user was found, try with username
            if user is None:
                user = form.get_user()
            
            if user is not None and user.check_password(password):
                login(request, user)
                return redirect('profil.html')
    else:
        form = AuthenticationForm(request)
    return render(request, 'connexion.html', {'form': form})


@login_required
def profile(request):
    user = request.user
    context = {
        'user': user
    }
    return render(request, 'profile.html', context)


def edit_profil(request):
    user = request.user
    user_type = ""

    if user.is_student:
        user_type = "etudiant"
        etudiant = Etudiant.objects.get(user=user)
        departements = Departement.objects.all()
        cursus_list = Cursus.objects.filter(departement=etudiant.departement)
        context = {
            'form_data': {
                'nom': user.nom,
                'prenom': user.prenom,
                # Ajoutez ici les autres champs du formulaire pour les étudiants
                'departement': etudiant.departement.id,
                'cursus': etudiant.cursus.id
            },
            'user_type': user_type,
            'departements': departements,
            'cursus_list': cursus_list
        }
    elif user.is_administratif:
        user_type = "administration"
        administratif = Administratif.objects.get(user=user)
        roles = Role.objects.all()
        context = {
            'form_data': {
                'nom': user.nom,
                'prenom': user.prenom,
                # Ajoutez ici les autres champs du formulaire pour les membres de l'administration
                'role': administratif.role.id
            },
            'user_type': user_type,
            'roles': roles
        }
    elif user.is_visiteur:
        user_type = "visiteur"
        context = {
            'form_data': {
                'nom': user.nom,
                'prenom': user.prenom,
                # Ajoutez ici les autres champs du formulaire pour les visiteurs
                'newsletter': user.newsletter
            },
            'user_type': user_type
        }
    else:
        context = {}

    return render(request, 'edit_profil.html', context)