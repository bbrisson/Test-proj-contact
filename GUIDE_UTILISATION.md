# Guide d'utilisation de l'interface graphique

## Aperçu de l'application

L'application Gestionnaire de Contacts offre une interface graphique simple et intuitive construite avec Tkinter.

## Fenêtre principale

### Layout
```
╔═══════════════════════════════════════════════════════════════╗
║               Gestionnaire de Contacts                        ║
╠═══════════════════════════════════════════════════════════════╣
║  Rechercher: [_____________________] [Effacer]                ║
╠═══════════════════════════════════════════════════════════════╣
║  ┌───────────────────────────────────────────────────────┐   ║
║  │ Nom             │ Email                 │ Téléphone   │   ║
║  ├───────────────────────────────────────────────────────┤   ║
║  │ Marie Curie     │ marie.curie@...       │ 0123456789  │   ║
║  │ Albert Einstein │ albert@physics.com    │ 0198765432  │   ║
║  │ Ada Lovelace    │ ada@computing.uk      │ 0155555555  │   ║
║  │                 │                       │             │   ║
║  └───────────────────────────────────────────────────────┘   ║
╠═══════════════════════════════════════════════════════════════╣
║  [Ajouter]  [Supprimer]                        [Quitter]      ║
╚═══════════════════════════════════════════════════════════════╝
```

### Fonctionnalités

1. **Barre de recherche** (en haut)
   - Recherche en temps réel
   - Filtre par nom, email ou téléphone
   - Bouton "Effacer" pour réinitialiser

2. **Tableau des contacts** (zone centrale)
   - Affichage des contacts dans un Treeview
   - 3 colonnes: Nom, Email, Téléphone
   - Scrollbar verticale si nécessaire
   - Sélection par clic

3. **Boutons d'action** (en bas)
   - **Ajouter**: Ouvre la fenêtre de dialogue
   - **Supprimer**: Supprime le contact sélectionné (avec confirmation)
   - **Quitter**: Sauvegarde et ferme l'application

## Fenêtre d'ajout de contact

### Layout
```
╔═══════════════════════════════════════════╗
║       Ajouter un contact                  ║
╠═══════════════════════════════════════════╣
║                                           ║
║  Nom:       [_____________________]       ║
║                                           ║
║  Email:     [_____________________]       ║
║                                           ║
║  Téléphone: [_____________________]       ║
║                                           ║
║         [Valider]  [Annuler]              ║
║                                           ║
╚═══════════════════════════════════════════╝
```

### Caractéristiques

- Fenêtre modale (bloque la fenêtre principale)
- Validation des champs (tous requis)
- Raccourcis clavier:
  - `Entrée`: Valider
  - `Échap`: Annuler
- Messages d'erreur si champs vides
- Centrée automatiquement à l'écran

## Workflow typique

1. **Lancement**: `python main.py`
   - Charge automatiquement contacts.json (ou crée un nouveau fichier)

2. **Ajouter un contact**:
   - Clic sur "Ajouter"
   - Remplir les champs
   - Clic sur "Valider" ou touche Entrée
   - Confirmation "Contact ajouté avec succès!"

3. **Rechercher un contact**:
   - Taper dans la barre de recherche
   - Résultats filtrés en temps réel

4. **Supprimer un contact**:
   - Sélectionner un contact dans le tableau
   - Clic sur "Supprimer"
   - Confirmer la suppression
   - Message "Contact supprimé avec succès!"

5. **Quitter**:
   - Clic sur "Quitter"
   - Sauvegarde automatique dans contacts.json

## Persistance des données

- **Fichier**: `contacts.json` (créé automatiquement)
- **Format**: JSON avec encodage UTF-8
- **Sauvegarde**: Automatique après chaque modification
- **Chargement**: Automatique au démarrage

## Messages utilisateur

L'application affiche des messages dans les cas suivants:
- ✓ "Contact ajouté avec succès!"
- ✓ "Contact supprimé avec succès!"
- ⚠ "Le nom est requis."
- ⚠ "L'email est requis."
- ⚠ "Le téléphone est requis."
- ⚠ "Veuillez sélectionner un contact à supprimer."
- ? "Voulez-vous vraiment supprimer ce contact?"

## Personnalisation possible

Le code est bien structuré et commenté, permettant facilement:
- Ajouter d'autres champs (adresse, notes, etc.)
- Modifier l'apparence (couleurs, tailles)
- Ajouter des fonctionnalités (export CSV, impression, etc.)
- Implémenter des filtres avancés
