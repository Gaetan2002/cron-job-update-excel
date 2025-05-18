from google_sheets.utils import get_gspread_client
# Importe la fonction utilitaire pour obtenir un client gspread authentifié.

def upload_to_google_sheet(data, spreadsheet_name, worksheet_name):
    # Déclare une fonction qui envoie des données (DataFrame pandas) dans une feuille Google Sheets.

    client = get_gspread_client()
    # Récupère un client gspread authentifié.

    try:
        spreadsheet = client.open(spreadsheet_name)
    except Exception:
        spreadsheet = client.create(spreadsheet_name)
    # Essaie d’ouvrir le Google Sheet par son nom ; s’il n’existe pas, le crée.

    try:
        worksheet = spreadsheet.worksheet(worksheet_name)
    except Exception:
        worksheet = spreadsheet.add_worksheet(title=worksheet_name, rows="100", cols="20")
    # Essaie d’ouvrir l’onglet (worksheet) par son nom ; s’il n’existe pas, le crée avec 100 lignes et 20 colonnes.

    worksheet.clear()
    # Vide tout le contenu de la feuille avant d’y écrire les nouvelles données.

    values = [list(data.columns)] + data.values.tolist()
    # Prépare les données à envoyer : la première ligne contient les noms de colonnes, suivie des valeurs du DataFrame.

    worksheet.update(values=values, range_name='A1')
    # Met à jour la feuille Google Sheets à partir de la cellule A1 avec toutes les données préparées.