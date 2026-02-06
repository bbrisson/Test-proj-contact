"""
Classe MainWindow pour la fenêtre principale de l'application.
"""

import tkinter as tk
from tkinter import ttk, messagebox
import os
from models.contact import Contact
from gui.dialogs import AddContactDialog


class MainWindow:
    """Fenêtre principale de l'application de gestion de contacts."""
    
    def __init__(self, contact_manager):
        """
        Initialise la fenêtre principale.
        
        Args:
            contact_manager (ContactManager): Le gestionnaire de contacts
        """
        self.contact_manager = contact_manager
        self.fichier_sauvegarde = "contacts.json"
        
        # Charger les contacts existants
        self.contact_manager.charger(self.fichier_sauvegarde)
        
        # Créer la fenêtre principale
        self.root = tk.Tk()
        self.root.title("Gestionnaire de Contacts")
        self.root.geometry("800x500")
        
        # Créer les widgets
        self._creer_widgets()
        
        # Actualiser l'affichage
        self._actualiser_liste()
        
        # Sauvegarder à la fermeture
        self.root.protocol("WM_DELETE_WINDOW", self._quitter)
    
    def _creer_widgets(self):
        """Crée les widgets de la fenêtre principale."""
        # Cadre supérieur pour la barre de recherche
        top_frame = tk.Frame(self.root, padx=10, pady=10)
        top_frame.pack(fill=tk.X)
        
        tk.Label(top_frame, text="Rechercher:").pack(side=tk.LEFT, padx=(0, 5))
        self.recherche_var = tk.StringVar()
        self.recherche_var.trace('w', lambda *args: self._rechercher())
        self.recherche_entry = tk.Entry(top_frame, textvariable=self.recherche_var, width=40)
        self.recherche_entry.pack(side=tk.LEFT, padx=(0, 10))
        
        # Bouton pour effacer la recherche
        tk.Button(top_frame, text="Effacer", command=self._effacer_recherche).pack(side=tk.LEFT)
        
        # Cadre central pour le tableau
        middle_frame = tk.Frame(self.root, padx=10, pady=(0, 10))
        middle_frame.pack(fill=tk.BOTH, expand=True)
        
        # Créer le Treeview (tableau)
        columns = ('Nom', 'Email', 'Téléphone')
        self.tree = ttk.Treeview(middle_frame, columns=columns, show='headings', height=15)
        
        # Définir les en-têtes
        self.tree.heading('Nom', text='Nom')
        self.tree.heading('Email', text='Email')
        self.tree.heading('Téléphone', text='Téléphone')
        
        # Définir les largeurs de colonnes
        self.tree.column('Nom', width=200)
        self.tree.column('Email', width=250)
        self.tree.column('Téléphone', width=150)
        
        # Scrollbar
        scrollbar = ttk.Scrollbar(middle_frame, orient=tk.VERTICAL, command=self.tree.yview)
        self.tree.configure(yscroll=scrollbar.set)
        
        # Placer le tableau et la scrollbar
        self.tree.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        
        # Cadre inférieur pour les boutons
        bottom_frame = tk.Frame(self.root, padx=10, pady=10)
        bottom_frame.pack(fill=tk.X)
        
        # Boutons
        tk.Button(bottom_frame, text="Ajouter", command=self._ajouter_contact, width=15).pack(side=tk.LEFT, padx=5)
        tk.Button(bottom_frame, text="Supprimer", command=self._supprimer_contact, width=15).pack(side=tk.LEFT, padx=5)
        tk.Button(bottom_frame, text="Quitter", command=self._quitter, width=15).pack(side=tk.RIGHT, padx=5)
    
    def _actualiser_liste(self, contacts=None):
        """
        Actualise l'affichage de la liste des contacts.
        
        Args:
            contacts (list, optional): Liste des contacts à afficher. 
                                      Si None, affiche tous les contacts.
        """
        # Effacer le contenu actuel
        for item in self.tree.get_children():
            self.tree.delete(item)
        
        # Utiliser tous les contacts si aucune liste n'est fournie
        if contacts is None:
            contacts = self.contact_manager.obtenir_contacts()
        
        # Ajouter les contacts au tableau
        for contact in contacts:
            self.tree.insert('', tk.END, values=(contact.nom, contact.email, contact.telephone))
    
    def _ajouter_contact(self):
        """Affiche la fenêtre de dialogue pour ajouter un contact."""
        dialog = AddContactDialog(self.root)
        result = dialog.show()
        
        if result:
            # Créer un nouveau contact
            contact = Contact(result['nom'], result['email'], result['telephone'])
            self.contact_manager.ajouter_contact(contact)
            
            # Sauvegarder et actualiser
            self.contact_manager.sauvegarder(self.fichier_sauvegarde)
            self._actualiser_liste()
            
            messagebox.showinfo("Succès", "Contact ajouté avec succès!")
    
    def _supprimer_contact(self):
        """Supprime le contact sélectionné."""
        selection = self.tree.selection()
        
        if not selection:
            messagebox.showwarning("Attention", "Veuillez sélectionner un contact à supprimer.")
            return
        
        # Confirmer la suppression
        if messagebox.askyesno("Confirmation", "Voulez-vous vraiment supprimer ce contact?"):
            # Obtenir l'index du contact sélectionné
            item = selection[0]
            index = self.tree.index(item)
            
            # Supprimer le contact
            self.contact_manager.supprimer_contact(index)
            
            # Sauvegarder et actualiser
            self.contact_manager.sauvegarder(self.fichier_sauvegarde)
            self._actualiser_liste()
            
            messagebox.showinfo("Succès", "Contact supprimé avec succès!")
    
    def _rechercher(self):
        """Recherche des contacts en fonction du texte saisi."""
        terme = self.recherche_var.get()
        
        if terme:
            # Rechercher et afficher les résultats
            resultats = self.contact_manager.rechercher(terme)
            self._actualiser_liste(resultats)
        else:
            # Afficher tous les contacts si la recherche est vide
            self._actualiser_liste()
    
    def _effacer_recherche(self):
        """Efface le champ de recherche et affiche tous les contacts."""
        self.recherche_var.set('')
        self._actualiser_liste()
    
    def _quitter(self):
        """Sauvegarde et quitte l'application."""
        self.contact_manager.sauvegarder(self.fichier_sauvegarde)
        self.root.destroy()
    
    def run(self):
        """Lance la boucle principale de l'application."""
        self.root.mainloop()
