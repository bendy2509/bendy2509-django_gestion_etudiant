from django.db import models

# Créez vos modèles ici.

class User(models.Model):
    """
    Modèle représentant un utilisateur avec un nom, un email et un mot de passe.
    """
    
    name = models.CharField(max_length=70)  # Champ pour le nom de l'utilisateur, longueur maximale de 70 caractères
    email = models.CharField(max_length=100)  # Champ pour l'email de l'utilisateur, longueur maximale de 100 caractères
    password = models.CharField(max_length=100)  # Champ pour le mot de passe de l'utilisateur, longueur maximale de 100 caractères
    
    def __str__(self):
        """
        Méthode pour représenter l'objet User sous forme de chaîne.
        Retourne le nom de l'utilisateur.
        """
        return self.name
