from django.shortcuts import get_object_or_404, render, HttpResponseRedirect
from .forms import StudentRegistration
from .models import User

# Créez vos vues ici.

def add_show(request):
    """
    Vue pour gérer l'ajout d'un nouvel étudiant et afficher la liste des étudiants.
    Si la méthode de la requête est POST, elle traite les données du formulaire et enregistre le nouvel étudiant.
    Sinon, elle affiche simplement le formulaire d'inscription et la liste des étudiants.
    """
    if request.method == 'POST':
        # Traiter le formulaire soumis
        fm = StudentRegistration(request.POST)
        if fm.is_valid():
            # Extraire les données nettoyées du formulaire
            name = fm.cleaned_data["name"]
            email = fm.cleaned_data["email"]
            password = fm.cleaned_data["password"]
            
            # Créer une nouvelle instance de User et l'enregistrer dans la base de données
            req = User(name=name, email=email, password=password)            
            req.save()
            
            # Réinitialiser le formulaire après une soumission réussie
            fm = StudentRegistration()
    else:
        # Afficher un formulaire vide pour les requêtes GET
        fm = StudentRegistration()
    
    # Récupérer tous les enregistrements d'étudiants dans la base de données
    student = User.objects.all()
    
    # Dictionnaire de contexte à passer au template
    context = {
        'form': fm,
        'student': student,
    }
    
    # Rendre le template avec le contexte fourni
    return render(request, 'student/addAndShow.html', context)

def delete_data(request, id):
    """
    Vue pour gérer la suppression d'un enregistrement d'étudiant.
    Si la méthode de la requête est POST, elle supprime l'étudiant avec l'ID donné.
    """
    if request.method == 'POST':
        # Récupérer l'enregistrement de l'étudiant par clé primaire (id)
        data_ = User.objects.get(pk=id)
        
        # Supprimer l'enregistrement de l'étudiant de la base de données
        data_.delete()
        
        # Rediriger vers la page d'accueil après la suppression
        return HttpResponseRedirect('/')

def update_data(request, id):
    """
    Vue pour gérer la mise à jour des informations d'un étudiant.
    Si la méthode de la requête est POST, elle traite les données du formulaire et met à jour l'étudiant.
    Sinon, elle affiche le formulaire pré-rempli avec les données existantes de l'étudiant.
    """
    if request.method == 'POST':
        # Récupérer l'instance de l'étudiant à mettre à jour
        pi = get_object_or_404(User, pk=id)

        # Créer un formulaire avec les données soumises et l'instance de l'étudiant
        form = StudentRegistration(request.POST, instance=pi)
        
        if form.is_valid():
            form.save()  # Sauvegarder les modifications
            return HttpResponseRedirect('/')
    else:
        # Récupérer l'instance de l'étudiant à mettre à jour
        pi = get_object_or_404(User, pk=id)

        # Créer un formulaire pré-rempli avec les données de l'étudiant
        form = StudentRegistration(instance=pi)
    
    # Dictionnaire de contexte à passer au template
    context = {
        'id': id,
        'form': form
    }
    
    # Rendre le template avec le contexte fourni
    return render(request, 'student/updatesStudent.html', context)
