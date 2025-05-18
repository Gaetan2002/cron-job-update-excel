import gspread
# Importe la bibliothèque gspread, qui permet de manipuler des feuilles Google Sheets en Python.

from oauth2client.service_account import ServiceAccountCredentials
# Importe la classe ServiceAccountCredentials, utilisée pour l’authentification avec un compte de service Google.

def get_gspread_client():
    # Déclare une fonction qui va retourner un client gspread authentifié.

    scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
    # Définit la portée des autorisations : accès aux feuilles Google Sheets et à Google Drive.

    creds = ServiceAccountCredentials.from_json_keyfile_name('credentials/credentials.json', scope)
    # Crée un objet d’authentification à partir du fichier JSON du compte de service (chemin relatif 'credentials/credentials.json') et de la portée définie.

    return gspread.authorize(creds)
    # Retourne un client gspread authentifié, prêt à manipuler des feuilles Google Sheets.