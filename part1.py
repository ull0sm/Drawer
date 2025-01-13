import pandas as pd
import math

def read_excel(file_path):
    # Read the Excel file
    df = pd.read_excel(file_path)
    return df

def create_groups(df, n):
    # Create groups of size n
    num_groups = math.ceil(len(df) / n)
    groups = [df[i * n:(i + 1) * n] for i in range(num_groups)]
    return groups

def write_to_excel(groups, output_file):
    # Write groups to a new Excel file
    with pd.ExcelWriter(output_file, engine='openpyxl') as writer:
        for idx, group in enumerate(groups):
            group.to_excel(writer, sheet_name=f'Pool_{idx + 1}', index=False)

def main():
    # Accept input parameters
    file_path = "trial.xlsx"
    n = 8
    
    # Process the Excel file
    df = read_excel(file_path)
    groups = create_groups(df, n)
    
    # Write the output to a new Excel file
    output_file = 'grouped_output.xlsx'
    write_to_excel(groups, output_file)
    print(f"Grouped data has been written to {output_file}")

if __name__ == "__main__":
    main()