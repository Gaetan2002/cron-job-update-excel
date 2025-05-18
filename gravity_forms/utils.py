import os
# Importe le module os pour accéder aux variables d’environnement du système.

from dotenv import load_dotenv
# Importe la fonction load_dotenv pour charger les variables d’environnement depuis un fichier .env.

from requests_oauthlib import OAuth1
# Importe la classe OAuth1, qui permet de gérer l’authentification OAuth 1.0a pour les requêtes HTTP.

# Charger les variables d'environnement depuis le .env
load_dotenv()
# Charge automatiquement les variables définies dans le fichier .env à la racine du projet dans les variables d’environnement du système.

def get_gf_oauth():
    # Déclare une fonction qui va préparer l’authentification OAuth pour l’API Gravity Forms.

    consumer_key = os.getenv('GF_CONSUMER_KEY')
    # Récupère la clé publique (consumer key) depuis les variables d’environnement.

    consumer_secret = os.getenv('GF_CONSUMER_SECRET')
    # Récupère la clé privée (consumer secret) depuis les variables d’environnement.

    if not consumer_key or not consumer_secret:
        raise ValueError("Les clés d'authentification ne sont pas définies dans les variables d'environnement.")
    # Si l’une des deux clés n’est pas trouvée, lève une erreur explicite.

    return OAuth1(
        consumer_key,
        client_secret=consumer_secret,
        signature_method='HMAC-SHA1',
        signature_type='AUTH_HEADER'
    )
    # Retourne un objet OAuth1 configuré avec les clés, prêt à être utilisé pour authentifier les requêtes HTTP vers l’API Gravity Forms.