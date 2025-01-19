import os
import pandas as pd
import math
from collections import defaultdict

def distribute_players(df, num_groups):
    """
    Distribute players into groups in ascending order of weight (WT),
    while minimizing players from the same school in the same group.
    """
    # Sort the DataFrame by weight (ascending)
    df = df.sort_values(by="WT").reset_index(drop=True)
    
    # Initialize empty groups
    groups = [pd.DataFrame(columns=df.columns) for _ in range(num_groups)]
    
    # Keep track of group sizes and school distribution
    group_sizes = [0] * num_groups
    school_counts = [{} for _ in range(num_groups)]
    
    for _, row in df.iterrows():
        # Find the group that best fits this player
        best_group = -1
        min_school_overlap = float('inf')
        
        for i in range(num_groups):
            school = row["School"]
            # Calculate how many players from the same school are in this group
            overlap = school_counts[i].get(school, 0)
            
            # Choose the group with the least overlap and balanced size
            if overlap < min_school_overlap or (overlap == min_school_overlap and group_sizes[i] < group_sizes[best_group]):
                min_school_overlap = overlap
                best_group = i
        
        # Add player to the selected group
        groups[best_group] = pd.concat([groups[best_group], pd.DataFrame([row])], ignore_index=True)
        group_sizes[best_group] += 1
        school_counts[best_group][row["School"]] = school_counts[best_group].get(row["School"], 0) + 1
    
    return groups

def divide_and_group(file_path, save_path, max_players=8):
    # Read the Excel file
    df = pd.read_excel(file_path)

    # Calculate the total number of players
    total_players = len(df)

    # Calculate the number of groups
    num_groups = math.ceil(total_players / max_players)

    # Distribute players into groups
    group_dfs = distribute_players(df, num_groups)

    # Create a new Excel writer
    dataset_name = os.path.splitext(os.path.basename(file_path))[0]
    output_path = os.path.join(save_path, f"{dataset_name}.xlsx")

    with pd.ExcelWriter(output_path, engine='openpyxl') as writer:
        for i, group_df in enumerate(group_dfs):
            # Write the group to a new sheet
            group_df.to_excel(writer, sheet_name=f"Group {i + 1}", index=False)

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
    input_directory = ".\\filtered_data\\sat"
    output_directory = ".\\groups"
    process_all_files(input_directory, output_directory)
    input_directory = ".\\filtered_data\\sun"
    output_directory = ".\\groups"
    process_all_files(input_directory, output_directory)
