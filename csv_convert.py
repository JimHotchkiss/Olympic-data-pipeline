import pandas as pd

excel_files = ['Athletes.xlsx', 'Coaches.xlsx', 'EntriesGender.xlsx', 'Medals.xlsx', 'Teams.xlsx']

def csv_convert(files):
    for file in files:
        # Read the excel file 
        df = pd.read_excel(file, sheet_name='Details')

        # Creaete the CSV file path by replacing the file extension
        csv_file_path = file.replace('xlsx', 'csv')

        # Convert to CSV
        df.to_csv(csv_file_path, index=False)



csv_convert(excel_files)