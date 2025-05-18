# Gravity Forms vers Google Sheets

Ce projet Python permet de récupérer automatiquement les inscriptions d’un formulaire Gravity Forms (WordPress) via l’API REST v2 (authentification OAuth 1.0a), de nettoyer les données (une seule donnée par cellule, suppression des colonnes vides) et de les envoyer directement dans une feuille Google Sheets.  
Aucun fichier CSV intermédiaire n’est utilisé : tout se fait en mémoire.

---

## Structure du projet

```
cron-job-update-excel
├── gravity_forms/
│   ├── fetch_entries.py      # Récupération des entrées Gravity Forms via l’API
│   └── utils.py              # Utilitaires pour l’API Gravity Forms (OAuth 1.0a)
├── processing/
│   └── clean_csv.py          # Nettoyage et formatage des données (fonctionne sur les entrées, pas sur un CSV)
├── google_sheets/
│   ├── upload.py             # Envoi des données dans Google Sheets
│   └── utils.py              # Authentification Google Sheets
├── main.py                   # Point d’entrée du projet
├── requirements.txt          # Dépendances Python
└── README.md                 # Documentation du projet
```

---

## Prérequis

- Python 3.7 ou supérieur
- Accès administrateur à l’API Gravity Forms sur votre site WordPress
- Un compte Google Cloud avec l’API Google Sheets activée

---

## Installation

1. **Clonez le dépôt** et placez-vous dans le dossier du projet.
2. **Créez un environnement virtuel** (recommandé) :

   Sous Windows :

   ```
   python -m venv .venv
   .\.venv\Scripts\activate
   ```

   Sous macOS/Linux :

   ```
   python3 -m venv .venv
   source .venv/bin/activate
   ```

3. **Installez les dépendances** :
   ```
   pip install -r requirements.txt
   ```

---

## Configuration Gravity Forms

1. Activez l’API REST v2 dans Gravity Forms.
2. Créez une clé API (publique et privée) dans les réglages Gravity Forms.
3. Ajoutez ces clés dans un fichier `.env` à la racine du projet :
   ```
   GF_CONSUMER_KEY=ta_clé_publique
   GF_CONSUMER_SECRET=ta_clé_privée
   ```
4. Vérifiez que le plugin Gravity Forms REST API est bien activé et à jour.

---

## Configuration Google Sheets

1. Rendez-vous sur le [Google Developers Console](https://console.developers.google.com/).
2. Créez un projet.
3. Activez l’API Google Sheets.
4. Créez des identifiants (Service Account) et téléchargez le fichier JSON.
5. Partagez votre feuille Google Sheets avec l’adresse e-mail du service account.

---

## Utilisation

1. Vérifiez que vos identifiants Google et Gravity Forms sont bien configurés.
2. Modifiez si besoin les variables `spreadsheet_name` et `worksheet_name` dans `main.py`.
3. Lancez le script principal :
   ```
   python main.py
   ```
   Les données seront récupérées, nettoyées et envoyées directement dans la feuille Google Sheets spécifiée.

---

## Remarques

- **Aucun fichier CSV n’est généré ni utilisé.**
- Le traitement se fait entièrement en mémoire pour plus de rapidité et de simplicité.
- Les colonnes vides sont supprimées automatiquement.
- L’authentification à Gravity Forms se fait via OAuth 1.0a (clés API).
- La pagination de l’API Gravity Forms est gérée automatiquement (page_size conseillé : 100).

---

## Licence

Ce projet est sous licence MIT.
