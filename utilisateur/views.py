from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth import authenticate
from utilisateur.forms import CustomUserCreationForm, StageForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login
from utilisateur.models import Stage
from django.http import HttpResponseForbidden

def inscription(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password1'])

            # Vérifier la valeur du champ type_utilisateur
            if user.type_utilisateur == 'ad':
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
                return redirect('profile')
    else:
        form = AuthenticationForm(request)
    return render(request, 'connexion.html', {'form': form})


@login_required(login_url='login')
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

@login_required(login_url='connexion')
def creer_stage(request):
    user = request.user
    if user.type_utilisateur != 'et':
        # Rediriger ou renvoyer une réponse d'interdiction d'accès
        return redirect('profile')

    if request.method == 'POST':
        form = StageForm(request.POST, request.FILES)
        if form.is_valid():
            stage = form.save(commit=False)
            stage.etudiant = user.nom  # Associer le nom de l'utilisateur courant au champ etudiant
            stage.owner = user.username 
            stage.save()
            user.stage = stage
            user.save()
            return redirect('profile')
    else:
        form = StageForm()
    
    return render(request, 'creer_stage.html', {'form': form})


@login_required(login_url='connexion')
def details_stage(request, stage_id):
    user = request.user
    if user.type_utilisateur != 'et':
        # Rediriger ou renvoyer une réponse d'interdiction d'accès
        return redirect('profile')
    stage = get_object_or_404(Stage, id=stage_id, owner=request.user.username)
    return render(request, 'details_stage.html', {'stage': stage})

@login_required(login_url='connexion')
def modifier_stage(request, stage_id):
    user = request.user
    if user.type_utilisateur != 'et':
        # Rediriger ou renvoyer une réponse d'interdiction d'accès
        return redirect('profile')
    stage = get_object_or_404(Stage, id=stage_id, owner=request.user.username)

    if request.method == 'POST':
        form = StageForm(request.POST, request.FILES, instance=stage)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = StageForm(instance=stage)
    
    return render(request, 'modifier_stage.html', {'form': form})

@login_required(login_url='connexion')
def supprimer_stage(request, stage_id):
    user = request.user
    if user.type_utilisateur != 'et':
        # Rediriger ou renvoyer une réponse d'interdiction d'accès
        return redirect('profile')
    stage = get_object_or_404(Stage, id=stage_id, owner=request.user.username)

    if request.method == 'POST':
        stage.delete()
        return redirect('profile')
    
    return render(request, 'supprimer_stage.html', {'stage': stage})