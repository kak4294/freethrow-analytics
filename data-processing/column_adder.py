import pandas as pd
import os

def get_datatype(dtype_str):
    dtype_str = dtype_str.lower()
    if dtype_str in ['int', 'integer']:
        return int
    elif dtype_str in ['float', 'double', 'decimal']:
        return float
    elif dtype_str in ['str', 'string', 'text']:
        return str
    elif dtype_str in ['bool', 'boolean']:
        return lambda x: str(x).lower() in ['true', '1', 'yes']
    else:
        raise ValueError(f"Unsupported datatype: {dtype_str}")

def process_file(csv_path, columns):
    if not os.path.isfile(csv_path):
        print(f"File not found: {csv_path}")
        return
    df = pd.read_csv(csv_path)
    for col_name, dtype, value in columns:
        df[col_name] = value
    base, ext = os.path.splitext(csv_path)
    new_path = f"{base}_updated_{ext}"
    df.to_csv(new_path, index=False)
    print(f"New file saved as: {new_path}")

def main():
    csv_paths = input('Enter the path(s) to the CSV file(s), comma separated: ').strip()
    csv_files = [p.strip() for p in csv_paths.split(',') if p.strip()]

    try:
        n_cols = int(input('How many columns do you want to add? '))
    except ValueError:
        print('Invalid number.')
        return

    columns = []
    for i in range(n_cols):
        col_name = input(f'Enter name for column #{i+1}: ').strip()
        dtype_str = input(f'Enter datatype for column "{col_name}" (int, float, str, bool): ').strip()
        value_str = input(f'Enter value to populate column "{col_name}": ').strip()
        try:
            dtype = get_datatype(dtype_str)
            value = dtype(value_str)
        except Exception as e:
            print(f'Error: {e}')
            return
        columns.append((col_name, dtype, value))

    for csv_path in csv_files:
        process_file(csv_path, columns)

if __name__ == '__main__':
    main()
