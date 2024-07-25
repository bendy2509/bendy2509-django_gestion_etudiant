# Django Student Management System CHC-L

Un système de gestion des étudiants du CHC-L construit avec Django. Ce projet fournit une interface utilisateur simple pour ajouter, afficher, mettre à jour et supprimer des informations sur les étudiants.

## Fonctionnalités

- **Ajouter un étudiant** : Formulaire pour enregistrer les informations de nouveaux étudiants.
- **Afficher les étudiants** : Liste de tous les étudiants enregistrés avec des options pour modifier et supprimer leurs informations.
- **Mettre à jour les informations des étudiants** : Formulaire pour modifier les informations existantes des étudiants.
- **Supprimer un étudiant** : Option pour supprimer les enregistrements d'étudiants.

## Prérequis

- Python 3.x
- Django

## Installation

1. **Clonez le repository** :
   ```bash
   git clone https://github.com/bendy2509/bendy2509-django_gestion_etudiant.git
   cd django_gestion_etudiant
   ```

2. **Créez et activez un environnement virtuel** :
   ```bash
   python -m venv env
   source env/bin/activate
   ```

3. **Installez les dépendances** :
   ```bash
   pip install -r requirements.txt
   ```

4. **Configurez la base de données** :
   Mettez à jour les paramètres de base de données dans le fichier `settings.py` si nécessaire.

5. **Appliquez les migrations** :
   ```bash
   python manage.py migrate
   ```

6. **Démarrez le serveur de développement** :
   ```bash
   python manage.py runserver
   ```

7. **Accédez à l'application** :
   Ouvrez un navigateur web et allez à `http://127.0.0.1:8000` pour accéder à l'application.

## Utilisation

### Ajouter un étudiant

1. Accédez à la page d'ajout d'étudiant.
2. Remplissez le formulaire avec les informations de l'étudiant.
3. Cliquez sur le bouton "Ajouter" pour enregistrer les informations.

### Afficher les étudiants

1. Accédez à la page des étudiants.
2. Visualisez la liste des étudiants enregistrés.
3. Utilisez les boutons "Modifier" et "Supprimer" pour gérer les informations des étudiants.

### Mettre à jour les informations des étudiants

1. Accédez à la page de mise à jour des informations de l'étudiant.
2. Modifiez les informations selon les besoins.
3. Cliquez sur le bouton "Modifier" pour enregistrer les modifications.

### Supprimer un étudiant

1. Accédez à la liste des étudiants.
2. Utilisez le bouton "Supprimer" à côté de l'étudiant que vous souhaitez supprimer.
3. Confirmez la suppression si nécessaire.

## Auteurs

- [Bendy SERVILUS](https://github.com/bendy2509)
