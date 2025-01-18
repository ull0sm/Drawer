import os
import pandas as pd
import math

def divide_and_group(file_path, save_path, max_players=8):
    # Read the Excel file
    df = pd.read_excel(file_path)

    # Calculate the total number of players
    total_players = len(df)

    # Calculate the number of groups
    num_groups = math.ceil(total_players / max_players)

    # Distribute players as evenly as possible
    base_group_size = total_players // num_groups
    extra_players = total_players % num_groups

    group_sizes = [base_group_size for _ in range(num_groups)]
    for i in range(extra_players):
        group_sizes[i] += 1

    # Create a new Excel writer
    dataset_name = os.path.splitext(os.path.basename(file_path))[0]
    output_path = os.path.join(save_path, f"{dataset_name}.xlsx")

    with pd.ExcelWriter(output_path, engine='openpyxl') as writer:
        start_idx = 0
        for i, group_size in enumerate(group_sizes):
            end_idx = start_idx + group_size
            
            # Slice the dataframe for the current group
            group_df = df.iloc[start_idx:end_idx]

            # Write the group to a new sheet
            group_df.to_excel(writer, sheet_name=f"Group {i + 1}", index=False)

            start_idx = end_idx

    print(f"Saved grouped dataset to {output_path}")

def process_all_files(input_dir, output_dir):
    # Ensure the output directory exists
    os.makedirs(output_dir, exist_ok=True)

    # Process each Excel file in the directory
    for file_name in os.listdir(input_dir):
        if file_name.endswith(".xlsx"):
            file_path = os.path.join(input_dir, file_name)
            divide_and_group(file_path, output_dir)

if __name__ == "__main__":
    input_directory = ".\\filtered_data\\sun"
    output_directory = ".\\groups"
    process_all_files(input_directory, output_directory)
