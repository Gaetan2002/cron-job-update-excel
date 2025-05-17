def process_csv_data(csv_file_path):
    import pandas as pd

    # Read the CSV file
    df = pd.read_csv(csv_file_path)

    # Remove empty columns
    df.dropna(axis=1, how='all', inplace=True)

    # Ensure each cell contains only one piece of data
    for col in df.columns:
        df[col] = df[col].astype(str).str.split(',').str[0]  # Adjust as needed for your data

    return df

# def upload_to_google_sheets(dataframe, spreadsheet_id, range_name, credentials):
#     from googleapiclient.discovery import build
#     from google.oauth2.service_account import Credentials

#     # Authenticate and create the service
#     creds = Credentials.from_service_account_file(credentials)
#     service = build(' sheets', 'v4', credentials=creds)

#     # Prepare the data for upload (including headers)
#     # Convert the DataFrame to a list of lists
#     # The first row will be the header
#     # The rest will be the data
#     values = [list(dataframe.columns)] + dataframe.values.tolist()
#     body = {
#         'values': values
#     }

#     # Upload the data to Google Sheets
#     service.spreadsheets().values().update(
#         spreadsheetId=spreadsheet_id,
#         range=range_name,
#         valueInputOption='RAW',
#         body=body
#     ).execute()