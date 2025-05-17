import csv
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import os
from utils import process_csv_data

def upload_to_google_sheet(data, spreadsheet_name, worksheet_name):
    # Define the scope and credentials for Google Sheets API
    scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
    creds = ServiceAccountCredentials.from_json_keyfile_name('root/cron-job-update-excel/csv-to-google-sheet/src/credentials.json', scope)
    client = gspread.authorize(creds)

    # Create or open the spreadsheet
    try:
        spreadsheet = client.open(spreadsheet_name)
    except gspread.SpreadsheetNotFound:
        spreadsheet = client.create(spreadsheet_name)

    # Select the worksheet
    try:
        worksheet = spreadsheet.worksheet(worksheet_name)
    except gspread.WorksheetNotFound:
        worksheet = spreadsheet.add_worksheet(title=worksheet_name, rows="100", cols="20")

    # Clear existing data in the worksheet
    worksheet.clear()

    # Convert DataFrame to list of lists (including headers)
    data = [list(data.columns)] + data.values.tolist()

    # Update the worksheet with new data
    worksheet.update(values=data, range_name='A1')

def main(csv_file_path, spreadsheet_name, worksheet_name):
    # Process the CSV file
    processed_data = process_csv_data(csv_file_path)

    # Upload the processed data to Google Sheets
    upload_to_google_sheet(processed_data, spreadsheet_name, worksheet_name)

if __name__ == "__main__":
    # Example usage
    csv_file_path = '/root/cron-job-update-excel/csv-to-google-sheet/src/csv_uploads/formulaire_4.csv'  # Replace with your CSV file path
    spreadsheet_name = 'STAGE TEST'  # Replace with your desired spreadsheet name
    worksheet_name = 'f1'  # Replace with your desired worksheet name
    main(csv_file_path, spreadsheet_name, worksheet_name)