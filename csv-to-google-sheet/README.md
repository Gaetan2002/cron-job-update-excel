# CSV to Google Sheet

This project provides a Python script that processes a CSV file to ensure each cell contains only one piece of data, removes any empty columns, and uploads the processed data to a Google Sheet.

## Project Structure

```
csv-to-google-sheet
├── src
│   ├── main.py        # Entry point of the application
│   └── utils.py       # Utility functions for processing CSV data
├── requirements.txt    # List of dependencies
└── README.md           # Project documentation
```

## Requirements

To run this project, you need to install the following dependencies:

- pandas: For handling CSV file operations.
- gspread: For interacting with Google Sheets.
- oauth2client: For Google API authentication.

You can install the required packages using pip:

```
pip install -r requirements.txt
```

## Setup Google Sheets API

1. Go to the [Google Developers Console](https://console.developers.google.com/).
2. Create a new project.
3. Enable the Google Sheets API for your project.
4. Create credentials (Service Account) and download the JSON file.
5. Share your Google Sheet with the email address of the service account.

## Running the Script

1. Place your CSV file in the appropriate directory.
2. Update the `main.py` file with the path to your CSV file and the Google Sheet ID.
3. Run the script:

```
python src/main.py
```

## License

This project is licensed under the MIT License.

## Virtual Environment Activation

Before running the script, ensure your virtual environment is activated. If you are using the command line, you can activate it with:

```
source .venv/Scripts/activate
```
