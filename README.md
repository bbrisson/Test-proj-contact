# Gestionnaire de Contacts

Une application simple de gestion de contacts avec interface graphique développée en Python avec Tkinter.

## Description

Ce projet est un gestionnaire de contacts permettant de :
- **Ajouter** de nouveaux contacts (nom, email, téléphone)
- **Supprimer** des contacts existants
- **Rechercher** des contacts par nom, email ou téléphone
- **Sauvegarder** automatiquement les contacts en JSON
- **Charger** les contacts au démarrage

## Installation

Aucune installation de dépendances externes n'est nécessaire. Le projet utilise uniquement des bibliothèques standards de Python :
- **Tkinter** (inclus avec Python)
- **JSON** (inclus avec Python)

### Prérequis
- Python 3.x

## Utilisation

Pour lancer l'application, exécutez simplement :

```bash
python main.py
```

### Exemple de données

Un fichier `example_contacts.json` est fourni avec quelques contacts d'exemple. Pour l'utiliser :
1. Renommez ou copiez `example_contacts.json` en `contacts.json`
2. Lancez l'application avec `python main.py`

Ou l'application créera automatiquement un nouveau fichier `contacts.json` vide au premier lancement.

## Structure du projet

```
Test-proj-contact/
├── main.py                  # Point d'entrée de l'application
├── models/
│   ├── __init__.py
│   ├── contact.py           # Classe Contact
│   └── contact_manager.py   # Classe ContactManager (gestion de la liste)
├── gui/
│   ├── __init__.py
│   ├── main_window.py       # Fenêtre principale (affichage et boutons)
│   └── dialogs.py           # Dialogue d'ajout de contact
├── contacts.json            # Fichier de sauvegarde (généré automatiquement)
└── README.md                # Documentation
```

## Fonctionnalités

### Fenêtre principale
- **Tableau de contacts** : Affiche tous les contacts avec nom, email et téléphone
- **Barre de recherche** : Filtre les contacts en temps réel
- **Bouton "Ajouter"** : Ouvre une fenêtre pour ajouter un nouveau contact
- **Bouton "Supprimer"** : Supprime le contact sélectionné (avec confirmation)
- **Bouton "Quitter"** : Sauvegarde et ferme l'application

### Ajout de contact
- Fenêtre modale avec validation des champs
- Champs requis : Nom, Email, Téléphone
- Touches raccourcies : Entrée (valider), Échap (annuler)

### Persistance des données
- Sauvegarde automatique après chaque ajout/suppression
- Chargement automatique au démarrage
- Format JSON pour faciliter l'édition manuelle si nécessaire

## Classes principales

### `Contact` (models/contact.py)
Représente un contact individuel avec ses attributs et méthodes de conversion.

### `ContactManager` (models/contact_manager.py)
Gère la liste des contacts et la persistance des données.

### `MainWindow` (gui/main_window.py)
Interface principale de l'application avec affichage et interactions.

### `AddContactDialog` (gui/dialogs.py)
Fenêtre de dialogue pour l'ajout de nouveaux contacts.

## Licence

Ce projet est un exemple éducatif.
