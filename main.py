from gravity_forms.fetch_entries import fetch_entries
from processing.clean_csv import process_entries
from google_sheets.upload import upload_to_google_sheet
from dotenv import load_dotenv
load_dotenv()
spreadsheet_name = 'STAGE TEST'
worksheet_name = 'f1'

if __name__ == "__main__":
    entries = fetch_entries()
    processed_data = process_entries(entries)
    upload_to_google_sheet(processed_data, spreadsheet_name, worksheet_name)