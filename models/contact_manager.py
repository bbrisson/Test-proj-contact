"""
Classe ContactManager pour gérer une liste de contacts avec persistance JSON.
"""

import json
from models.contact import Contact


class ContactManager:
    """Gère une liste de contacts avec sauvegarde/chargement JSON."""
    
    def __init__(self):
        """Initialise le gestionnaire avec une liste vide de contacts."""
        self.contacts = []
    
    def ajouter_contact(self, contact):
        """
        Ajoute un contact à la liste.
        
        Args:
            contact (Contact): Le contact à ajouter
        """
        self.contacts.append(contact)
    
    def supprimer_contact(self, index):
        """
        Supprime un contact de la liste par son index.
        
        Args:
            index (int): L'index du contact à supprimer
        """
        if 0 <= index < len(self.contacts):
            del self.contacts[index]
    
    def obtenir_contacts(self):
        """
        Retourne la liste de tous les contacts.
        
        Returns:
            list: Liste des contacts
        """
        return self.contacts
    
    def rechercher(self, terme):
        """
        Recherche des contacts contenant le terme dans nom, email ou téléphone.
        
        Args:
            terme (str): Le terme de recherche
            
        Returns:
            list: Liste des contacts correspondants
        """
        terme = terme.lower()
        resultats = []
        for contact in self.contacts:
            if (terme in contact.nom.lower() or 
                terme in contact.email.lower() or 
                terme in contact.telephone.lower()):
                resultats.append(contact)
        return resultats
    
    def sauvegarder(self, fichier):
        """
        Sauvegarde les contacts dans un fichier JSON.
        
        Args:
            fichier (str): Chemin du fichier de sauvegarde
        """
        with open(fichier, 'w', encoding='utf-8') as f:
            data = [contact.to_dict() for contact in self.contacts]
            json.dump(data, f, ensure_ascii=False, indent=2)
    
    def charger(self, fichier):
        """
        Charge les contacts depuis un fichier JSON.
        
        Args:
            fichier (str): Chemin du fichier à charger
        """
        try:
            with open(fichier, 'r', encoding='utf-8') as f:
                data = json.load(f)
                self.contacts = [Contact.from_dict(item) for item in data]
        except FileNotFoundError:
            # Si le fichier n'existe pas, on commence avec une liste vide
            self.contacts = []
