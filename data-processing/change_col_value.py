import pandas as pd
import os

def main():
    csv_path = input('Enter the path to the CSV file: ').strip()
    if not os.path.isfile(csv_path):
        print(f"File not found: {csv_path}")
        return
    
    df = pd.read_csv(csv_path)
    
    df['Season'] = df['Season'].apply(custom_transformation)
        
    base, ext = os.path.splitext(csv_path)
    new_path = f"{base}_sliced_{'Season'}{ext}"
    df.to_csv(new_path, index=False)
    print(f"Modified file saved as: {new_path}")
    

def custom_transformation(value):
    s = str(value)
    chars = list(s)
    
    if len(chars) == 6:
        chars[3] = chars[5]
        chars[4] = chars[6]
    
    value = ''.join(chars[:4])
    
    return value

if __name__ == '__main__':
    main()
