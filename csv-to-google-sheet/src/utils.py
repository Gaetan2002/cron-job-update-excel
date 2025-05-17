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