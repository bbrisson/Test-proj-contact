"""
Classe AddContactDialog pour la fenêtre de dialogue d'ajout de contact.
"""

import tkinter as tk
from tkinter import messagebox


class AddContactDialog:
    """Fenêtre de dialogue modale pour ajouter un nouveau contact."""
    
    def __init__(self, parent):
        """
        Initialise la fenêtre de dialogue.
        
        Args:
            parent: La fenêtre parente
        """
        self.result = None
        self.dialog = tk.Toplevel(parent)
        self.dialog.title("Ajouter un contact")
        self.dialog.geometry("400x200")
        self.dialog.resizable(False, False)
        
        # Rendre la fenêtre modale
        self.dialog.transient(parent)
        self.dialog.grab_set()
        
        # Créer les widgets
        self._creer_widgets()
        
        # Centrer la fenêtre
        self.dialog.update_idletasks()
        x = (self.dialog.winfo_screenwidth() // 2) - (400 // 2)
        y = (self.dialog.winfo_screenheight() // 2) - (200 // 2)
        self.dialog.geometry(f"+{x}+{y}")
    
    def _creer_widgets(self):
        """Crée les widgets de la fenêtre de dialogue."""
        # Cadre principal avec padding
        main_frame = tk.Frame(self.dialog, padx=20, pady=20)
        main_frame.pack(fill=tk.BOTH, expand=True)
        
        # Champ Nom
        tk.Label(main_frame, text="Nom:", width=10, anchor='w').grid(row=0, column=0, sticky='w', pady=5)
        self.nom_entry = tk.Entry(main_frame, width=30)
        self.nom_entry.grid(row=0, column=1, pady=5)
        self.nom_entry.focus()
        
        # Champ Email
        tk.Label(main_frame, text="Email:", width=10, anchor='w').grid(row=1, column=0, sticky='w', pady=5)
        self.email_entry = tk.Entry(main_frame, width=30)
        self.email_entry.grid(row=1, column=1, pady=5)
        
        # Champ Téléphone
        tk.Label(main_frame, text="Téléphone:", width=10, anchor='w').grid(row=2, column=0, sticky='w', pady=5)
        self.telephone_entry = tk.Entry(main_frame, width=30)
        self.telephone_entry.grid(row=2, column=1, pady=5)
        
        # Cadre pour les boutons
        button_frame = tk.Frame(main_frame)
        button_frame.grid(row=3, column=0, columnspan=2, pady=20)
        
        # Boutons Valider et Annuler
        tk.Button(button_frame, text="Valider", command=self._valider, width=10).pack(side=tk.LEFT, padx=5)
        tk.Button(button_frame, text="Annuler", command=self._annuler, width=10).pack(side=tk.LEFT, padx=5)
        
        # Lier la touche Entrée à la validation
        self.dialog.bind('<Return>', lambda e: self._valider())
        self.dialog.bind('<Escape>', lambda e: self._annuler())
    
    def _valider(self):
        """Valide les données saisies et ferme la fenêtre."""
        nom = self.nom_entry.get().strip()
        email = self.email_entry.get().strip()
        telephone = self.telephone_entry.get().strip()
        
        # Validation basique : champs non vides
        if not nom:
            messagebox.showwarning("Validation", "Le nom est requis.", parent=self.dialog)
            self.nom_entry.focus()
            return
        
        if not email:
            messagebox.showwarning("Validation", "L'email est requis.", parent=self.dialog)
            self.email_entry.focus()
            return
        
        if not telephone:
            messagebox.showwarning("Validation", "Le téléphone est requis.", parent=self.dialog)
            self.telephone_entry.focus()
            return
        
        # Stocker les résultats et fermer
        self.result = {
            'nom': nom,
            'email': email,
            'telephone': telephone
        }
        self.dialog.destroy()
    
    def _annuler(self):
        """Annule et ferme la fenêtre sans sauvegarder."""
        self.result = None
        self.dialog.destroy()
    
    def show(self):
        """
        Affiche la fenêtre de dialogue et attend sa fermeture.
        
        Returns:
            dict or None: Dictionnaire avec les données saisies ou None si annulé
        """
        self.dialog.wait_window()
        return self.result
