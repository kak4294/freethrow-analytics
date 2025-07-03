import pandas as pd
import os

def process_csv(csv_path):
    if not os.path.isfile(csv_path):
        print(f"File not found: {csv_path}")
        return

    # Read the CSV with two header rows, no header so we can process manually
    df = pd.read_csv(csv_path, header=None)

    # The first two rows are headers
    distance_row = df.iloc[0]
    stat_row = df.iloc[1]

    # Build new headers
    new_headers = []
    current_distance = ''
    distance_map = {
        'Less than 5ft.': '5less',
        '5-9 ft.': '5to9',
        '10-14 ft.': '10to14',
        '15-19 ft.': '15to19',
        '20-24 ft.': '20to24',
        '25-29 ft.': '25to29',
        '': ''
    }
    for dist, stat in zip(distance_row, stat_row):
        if pd.notna(dist) and dist != '':
            current_distance = distance_map.get(dist, dist)
        if current_distance:
            new_headers.append(f"{stat}_{current_distance}" if stat not in ['Player', 'Team', 'Age'] else stat)
        else:
            new_headers.append(stat)

    # Drop the first two rows and set new headers
    df = df.iloc[2:].reset_index(drop=True)
    df.columns = new_headers

    base, ext = os.path.splitext(csv_path)
    new_path = f"{base}_transformed{ext}"
    df.to_csv(new_path, index=False)
    print(f"Transformed file saved as: {new_path}")

def main():
    csv_paths = input('Enter the path(s) to the CSV file(s), comma separated: ').strip()
    files = [p.strip() for p in csv_paths.split(',') if p.strip()]
    for csv_path in files:
        process_csv(csv_path)

if __name__ == '__main__':
    main()
