import os
import glob
import pandas as pd
import mysql.connector
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

DB_HOST = os.getenv('DB_HOST')
DB_USER = os.getenv('DB_USER')
DB_PASSWORD = os.getenv('DB_PASSWORD')
DB_NAME = os.getenv('DB_NAME')
TABLE_NAME = os.getenv('TABLE_NAME') 


def get_mysql_connection():
    return mysql.connector.connect(
        host=DB_HOST,
        user=DB_USER,
        password=DB_PASSWORD,
        database=DB_NAME
    )

def import_csv_to_mysql(csv_file, conn, table_name):
    df = pd.read_csv(csv_file)
    cursor = conn.cursor()
    cols = ','.join([f'`{col}`' for col in df.columns])
    placeholders = ','.join(['%s'] * len(df.columns))
    insert_stmt = f"INSERT INTO {table_name} ({cols}) VALUES ({placeholders});"
    for row in df.itertuples(index=False, name=None):
        cursor.execute(insert_stmt, row)
    conn.commit()
    cursor.close()
    print(f"Imported {csv_file} into {table_name}")

def main():
    directory = input('Enter the directory containing CSV files: ').strip()
    if not os.path.isdir(directory):
        print(f"Directory not found: {directory}")
        return
    csv_files = glob.glob(os.path.join(directory, '*.csv'))
    if not csv_files:
        print('No CSV files found in the directory.')
        return
    conn = get_mysql_connection()
    for csv_file in csv_files:
        import_csv_to_mysql(csv_file, conn, TABLE_NAME)
    conn.close()
    print('All files imported successfully.')

if __name__ == '__main__':
    main()
