import pandas as pd
import os

# Ensure filtered_data directory exists
if not (os.path.exists("./filtered_data") & os.path.exists("./filtered_data/sun") & os.path.exists(".\\filtered_data\\sat")):
    os.makedirs("./filtered_data",exist_ok=True)
    os.makedirs("./filtered_data/sun",exist_ok=True)
    os.makedirs("./filtered_data/sat",exist_ok=True)

# Function to filter and create the Excel sheets
def create_filtered_excel(input_file):
    # Load the data from the Excel file
    df = pd.read_excel(input_file)
    print(f"Loaded {len(df)} rows from the input file.")

    # Define age group ranges for each belt type
    age_groups = {
        'WHITE': [(0, 5), (6, 6), (7, 7), (8, 8), (9, 9), (10, 10), (11, 11), (12, 12), (13, 13), (14, 14), (15, 15), (16, float('inf'))],
        'YELLOW': [(0, 5), (6, 6), (7, 7), (8, 8), (9, 9), (10, 10), (11, 11), (12, 12), (13, 13), (14, 14), (15, 15), (16, float('inf'))],
        'BLUE': [(0, 5), (6, 6), (7, 7), (8, 8), (9, 9), (10, 10), (11, 11), (12, 12), (13, 13), (14, 14), (15, 15), (16, float('inf'))],
        'PURPLE': [(0, 5), (6, 6), (7, 7), (8, 8), (9, 9), (10, 10), (11, 11), (12, 12), (13, 13), (14, 14), (15, 15), (16, float('inf'))],
        'GREEN': [(0, 5), (6, 6), (7, 7), (8, 8), (9, 9), (10, 10), (11, 11), (12, 12), (13, 13), (14, 14), (15, 15), (16, float('inf'))],
        'BROWN': [(7, 7), (8, 8), (9, 9), (10, 10), (11, 11), (12, 12), (13, 13), (14, 14), (15, 15), (16, float('inf'))],
        'BLACK': [(7, 7), (8, 8), (9, 9), (10, 10), (11, 11), (12, 12), (13, 13), (14, 14), (15, 15), (16, float('inf'))],
    }
    
    # Filter based on conditions
    for sex in ['M', 'F']:
        for day in ['SUN', 'SAT']:
            # Filter rows based on SEX and DAY
            filtered_df = df[(df['SEX'] == sex) & (df['DAY'] == day)]
            print(f"Filtered {len(filtered_df)} rows for SEX={sex} and DAY={day}.")

            for belt in ['WHITE', 'YELLOW', 'BLUE', 'PURPLE', 'GREEN', 'BROWN', 'BLACK']:
                # Filter data based on Belt
                belt_df = filtered_df[filtered_df['BELT'] == belt]
                print(f"  Filtered {len(belt_df)} rows for BELT={belt}.")

                for age_range in age_groups[belt]:
                    # Filter based on age range
                    age_condition = (belt_df['AGE'] >= age_range[0]) & (belt_df['AGE'] <= age_range[1])
                    age_filtered_df = belt_df[age_condition]
                    
                    if not age_filtered_df.empty:
                        # Determine age group label
                        if age_range[1] == float('inf'):
                            age_group = f"Above {age_range[0]}"
                        else:
                            age_group = str(age_range[0])
                        
                        # Create file name in the format: BELT_AGE_SEX_DAY.xlsx
                        if day == "SAT":
                            file_name = f"./filtered_data/sat/{belt.upper()}_{age_group}_{sex}_{day}.xlsx"
                        if day == "SUN":
                            file_name = f"./filtered_data/sun/{belt.upper()}_{age_group}_{sex}_{day}.xlsx"
                        
                        # Save the filtered data to an Excel file
                        age_filtered_df.to_excel(file_name, index=False)
                        print(f"Created file: {file_name}")

# Input file containing the data
input_file = './Demo_Run.xlsx'

# Call the function to process and create Excel files
create_filtered_excel(input_file)