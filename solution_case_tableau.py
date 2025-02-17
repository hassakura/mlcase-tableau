import pandas as pd
import os
import logging


CSV_FILE_NAME = "API_Download_DS2_en_csv_v2_69720.csv"
CURRENT_FOLDER = os.path.dirname(os.path.abspath(__file__))

log_file_path = os.path.join(CURRENT_FOLDER, "run_queries_case_tableau.log")

CSV_FILE_PATH = os.path.join(CURRENT_FOLDER, CSV_FILE_NAME)

logging.basicConfig(
    level = logging.INFO,
    format = '%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers = [
        logging.FileHandler(log_file_path),
        logging.StreamHandler()
    ])

def import_csv_with_header_row_3(filepath):
    """
        Receives a String filepath with the path to the CSV and returns the content as a Pandas DataFrame with the header from the 3rd row.

        Returns None if an error occurs
    """

    try:
        logging.info(f"Reading CSV from {filepath}.")
        df = pd.read_csv(filepath, header = 2)  # header = 2 means the 3rd row
        return df
    except Exception as e:
        logging.error(f"Error at import CSV: {e}")
        return None

df = import_csv_with_header_row_3(CSV_FILE_PATH)

# Dict with the final columns names
final_columns = {
        'Country Name': "country",
        'Country Code': "country_code",
        'Indicator Name': "indicator_name",
        'Indicator Code': "indicator_id"
    }

# Pivoted DataFrame. Original is a column for each Year. The pivoted DataFrame has the year as a Column.
pivoted_df = (
    df
        .set_index(['Country Name', 'Country Code', 'Indicator Name', 'Indicator Code'])
        .rename_axis(columns='year')
        .stack().reset_index(name='value')
        .rename(columns = final_columns)
        .loc[:, ['indicator_id', 'indicator_name', 'country', 'country_code', 'year', 'value']]
)

pivoted_df['year'] = pd.to_numeric(pivoted_df['year'], errors='coerce').astype('Int64')

pivoted_df.to_excel("tableau_case_all.xlsx", index = False)