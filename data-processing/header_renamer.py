import pandas as pd
import os
import re
import glob

def process_csv_file(csv_path):
    """Process a single CSV file and rename its headers."""
    print(f"\nProcessing: {csv_path}")
    
    if not os.path.isfile(csv_path):
        print(f"File not found: {csv_path}")
        return False

    try:
        # Read the CSV with multi-level headers
        df = pd.read_csv(csv_path, header=[0, 1])
        
        # Define the zone mappings
        zone_mappings = {
            'Restricted Area': '_RestrictA',
            'In The Paint(Non-RA)': '_PaintNonRA',
            'Mid-Range': '_MidR',
            'Left Corner 3.': '_LCorn3',
            'Right Corner 3.': '_RCorn3',
            'Corner 3': '_Corn3',
            'Above the Break 3.': '_AboveBreak3'
        }
        
        new_columns = []
        current_zone_suffix = None
        
        for col in df.columns:
            # col is a tuple like ('Restricted Area', 'FGM') or ('Unnamed: 0_level_0', 'Player')
            zone_name = col[0]
            stat_name = col[1]
            
            # Handle the first few columns (Player, Team, Age)
            if zone_name in ['Player', 'Team', 'Age'] or (stat_name in ['Player', 'Team', 'Age'] and 'Unnamed' in zone_name):
                new_col = stat_name
                current_zone_suffix = None  # Reset zone tracking for non-zone columns
            else:
                # Check if this is a new zone
                if zone_name in zone_mappings:
                    current_zone_suffix = zone_mappings[zone_name]
                    new_col = f"{stat_name}{current_zone_suffix}"
                elif 'Unnamed' in zone_name and current_zone_suffix:
                    # This is a continuation of the current zone (FGA or FG% column)
                    new_col = f"{stat_name}{current_zone_suffix}"
                else:
                    # Fallback for any unexpected columns
                    new_col = f"{stat_name}_{zone_name}" if not 'Unnamed' in zone_name else stat_name
            
            new_columns.append(new_col)
            if str(col) != new_col:
                print(f"  Renamed: {col} -> {new_col}")
        
        # Create new DataFrame with single-level column names
        df.columns = new_columns
        
        # Save the renamed file
        base, ext = os.path.splitext(csv_path)
        new_path = f"{base}_renamed{ext}"
        df.to_csv(new_path, index=False)
        print(f"  Renamed file saved as: {new_path}")
        return True
        
    except Exception as e:
        print(f"  Error processing {csv_path}: {str(e)}")
        return False

def main():
    path_input = input('Enter file path(s), directory path, or comma-separated file paths: ').strip()
    
    csv_files = []
    
    # Check if input is a directory
    if os.path.isdir(path_input):
        csv_files = glob.glob(os.path.join(path_input, "*.csv"))
        if not csv_files:
            print(f"No CSV files found in directory: {path_input}")
            return
        print(f"Found {len(csv_files)} CSV files in directory: {path_input}")
    
    # Check if input contains multiple files (comma-separated)
    elif ',' in path_input:
        csv_files = [path.strip() for path in path_input.split(',')]
        print(f"Processing {len(csv_files)} files...")
    
    # Single file
    else:
        csv_files = [path_input]
    
    # Process each file
    successful = 0
    failed = 0
    
    for csv_path in csv_files:
        if process_csv_file(csv_path):
            successful += 1
        else:
            failed += 1
    
    print(f"\nProcessing complete!")
    print(f"Successfully processed: {successful} files")
    if failed > 0:
        print(f"Failed to process: {failed} files")

if __name__ == '__main__':
    main() 