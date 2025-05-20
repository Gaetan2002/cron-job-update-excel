import requests
# Importe la bibliothèque requests pour faire des requêtes HTTP.

from datetime import datetime
#Importe la classe datetime pour manipuler les dates et heures.

from .utils import get_gf_oauth
# Importe la fonction get_gf_oauth du fichier utils.py pour gérer l’authentification OAuth1 à l’API Gravity Forms.

FIELD_MAP = {
    "id": "Id",
    "date_created": "créé le",
    "1.3": "Prénom",
    "1.6": "Nom",
    "25": "Année de naissance",
    "3": "Email",
    "7": "Téléphone",
    "5": "Genre",
    "4": "Stages 2025",
    "6": "Club",
    "8": "Grade",
    "9": "Logement",
    "10": "Repas",
    "21": "Méthode de paiement",
    "12": "Photo",
    "20.1": "Newsletters Email",
    "24.1": "Newsletter SMS",
    "23": "Montant",
}

def map_entry_fields(entry):
    # Transforme les clés Gravity Forms en noms lisibles
    return {FIELD_MAP[k]: entry[k] for k in FIELD_MAP if k in entry}

def fetch_entries():
    # Déclare la fonction principale qui va récupérer toutes les entrées du formulaire Gravity Forms.

    form_id = 4
    # Identifiant du formulaire Gravity Forms à interroger.

    all_entries = []
    # Liste qui va contenir toutes les entrées récupérées.

    seen_ids = set()
    # Ensemble pour stocker les IDs déjà vus (évite les doublons).

    page = 1
    # Numéro de la page courante pour la pagination.

    page_size = 100
    # Nombre d’entrées à récupérer par page (limite de l’API, 100 conseillé).

    max_pages = 200  # Sécurité
    # Nombre maximum de pages à parcourir (évite les boucles infinies).

    base_url = "https://navajowhite-wren-298423.hostingersite.com/wp-json/gf/v2/entries"
    # URL de base de l’API Gravity Forms pour récupérer les entrées.

    for _ in range(max_pages):
        # Boucle sur chaque page jusqu’à max_pages.

        params = {
            "form_ids": form_id,
            "paging[current_page]": page,
            "paging[page_size]": page_size,
        }
        # Prépare les paramètres de la requête : identifiant du formulaire, numéro de page, taille de page.

        auth = get_gf_oauth()
        # Récupère l’objet d’authentification OAuth1.

        headers = {"Content-Type": "application/json"}
        # Définit l’en-tête HTTP pour indiquer qu’on attend du JSON.

        response = requests.get(base_url, headers=headers, auth=auth, params=params)
        # Effectue la requête GET à l’API Gravity Forms avec l’URL, les en-têtes, l’authentification et les paramètres.

        print("Status:", response.status_code)
        # Affiche le code de statut HTTP de la réponse (utile pour le debug).

        response.raise_for_status()
        # Lève une exception si la requête a échoué (statut HTTP >= 400).

        data = response.json()
        # Convertit la réponse JSON en dictionnaire Python.

        entries = data.get('entries', [])
        # Récupère la liste des entrées dans la réponse (clé 'entries').

        total_count = data.get('total_count', 0)
        # Récupère le nombre total d’entrées disponibles (clé 'total_count').

        print(f"Page {page} : {len(entries)} entrées récupérées")
        # Affiche combien d’entrées ont été récupérées pour cette page.

        new_entries = [e for e in entries if e['id'] not in seen_ids]
        # Filtre les entrées pour ne garder que celles dont l’ID n’a pas encore été vu (évite les doublons).

        if not new_entries:
            print("Aucune nouvelle entrée, arrêt de la boucle.")
            break
        # Si aucune nouvelle entrée n’a été trouvée, on arrête la boucle (fin de la pagination ou doublons).

        for e in new_entries:
            seen_ids.add(e['id'])
        # Ajoute chaque nouvel ID à l’ensemble des IDs vus.

        all_entries.extend(new_entries)
        # Ajoute les nouvelles entrées à la liste globale.

        if len(entries) < page_size or len(all_entries) >= total_count:
            break
        # Si on a récupéré moins d’entrées que la taille de page (fin des données) ou tout le total, on arrête.

        page += 1
        # Passe à la page suivante pour la prochaine itération.

    print(f"Total récupéré (sans doublons) : {len(all_entries)}")
    # Affiche le nombre total d’entrées récupérées sans doublons.

    # Affiche la date actuelle détaillée après la récupération des données
    now = datetime.now()
    print("Date d'exécution :", now.strftime("%Y-%m-%d %H:%M:%S"))

    # Transforme les clés Gravity Forms en noms lisibles avant de retourner
    mapped_entries = [map_entry_fields(e) for e in all_entries]
    return mapped_entries
    # Retourne la liste complète des entrées avec noms de colonnes lisibles.

if __name__ == "__main__":
    # Si le fichier est exécuté directement (pas importé comme module) :

    entries = fetch_entries()
    # Appelle la fonction pour récupérer toutes les entrées.

    # Affiche uniquement le nombre d’entrées récupérées, pas leur contenu complet
    print(f"{len(entries)} entrées récupérées et prêtes à être envoyées à Google Sheets.")