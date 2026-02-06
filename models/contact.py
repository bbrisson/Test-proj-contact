"""
Classe Contact pour représenter un contact avec nom, email et téléphone.
"""

class Contact:
    """Représente un contact avec nom, email et téléphone."""
    
    def __init__(self, nom, email, telephone):
        """
        Initialise un nouveau contact.
        
        Args:
            nom (str): Le nom du contact
            email (str): L'adresse email du contact
            telephone (str): Le numéro de téléphone du contact
        """
        self.nom = nom
        self.email = email
        self.telephone = telephone
    
    def __str__(self):
        """Retourne une représentation textuelle du contact."""
        return f"{self.nom} - {self.email} - {self.telephone}"
    
    def to_dict(self):
        """
        Convertit le contact en dictionnaire.
        
        Returns:
            dict: Dictionnaire contenant les données du contact
        """
        return {
            'nom': self.nom,
            'email': self.email,
            'telephone': self.telephone
        }
    
    @classmethod
    def from_dict(cls, data):
        """
        Crée un contact depuis un dictionnaire.
        
        Args:
            data (dict): Dictionnaire contenant les données du contact
            
        Returns:
            Contact: Une nouvelle instance de Contact
        """
        return cls(data['nom'], data['email'], data['telephone'])
