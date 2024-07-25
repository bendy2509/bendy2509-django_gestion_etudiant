from django.core import validators
from django import forms
from .models import User

class StudentRegistration(forms.ModelForm):
    """
    Formulaire de modèle pour l'inscription des étudiants.
    Utilise le modèle User et spécifie les champs à inclure et leurs widgets.
    """
    
    class Meta:
        model = User  # Modèle à utiliser pour ce formulaire
        fields = ['name', 'email', 'password']  # Champs à inclure dans le formulaire
        
        # Widgets pour personnaliser l'apparence des champs du formulaire
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),  # Champ de texte avec la classe CSS 'form-control'
            'email': forms.EmailInput(attrs={'class': 'form-control'}),  # Champ d'email avec la classe CSS 'form-control'
            'password': forms.PasswordInput(attrs={'class': 'form-control'}, render_value=True),  # Champ de mot de passe avec la classe CSS 'form-control'
        }
