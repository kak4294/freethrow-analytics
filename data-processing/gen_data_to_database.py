import os
import pandas as pd
import mysql.connector
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

DB_HOST = os.getenv('DB_HOST')
DB_USER = os.getenv('DB_USER')
DB_PASSWORD = os.getenv('DB_PASSWORD')
DB_NAME = os.getenv('DB_NAME')
TABLE_NAME = os.getenv('GEN_TABLE_NAME')

def get_mysql_connection():
    return mysql.connector.connect(
        host=DB_HOST,
        user=DB_USER,
        password=DB_PASSWORD,
        database=DB_NAME
    )

def import_csv_to_mysql(csv_file, conn, table_name):
    df = pd.read_csv(csv_file)

    df = df.loc[:, ~df.columns.isna()]  
    df = df.dropna(how='all')  
    df = df.fillna(0)  # Long bug: MAKE SURE TO ALWAYS REASSIGN THE DF TO THE NEW DF

    print("Columns:", df.columns.tolist())
    print("First row:", df.iloc[0].tolist())

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
    csv_path = input('Enter the path to the CSV file: ').strip()
    if not os.path.isfile(csv_path):
        print(f"File not found: {csv_path}")
        return

    conn = get_mysql_connection()
    import_csv_to_mysql(csv_path, conn, TABLE_NAME)
    conn.close()
    print('File imported successfully.')

if __name__ == '__main__':
    main()
