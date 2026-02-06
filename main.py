"""
Point d'entrée de l'application Gestionnaire de Contacts.
"""

from models.contact_manager import ContactManager
from gui.main_window import MainWindow


def main():
    """Lance l'application."""
    # Créer l'instance du gestionnaire de contacts
    contact_manager = ContactManager()
    
    # Créer et lancer la fenêtre principale
    app = MainWindow(contact_manager)
    app.run()


if __name__ == "__main__":
    main()
