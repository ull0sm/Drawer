import os
import pandas as pd
import math
from collections import defaultdict

def distribute_players(df, num_groups):
    """
    Distribute players into groups while attempting to separate players from the same school.
    """
    groups = [[] for _ in range(num_groups)]
    school_players = defaultdict(list)

    # Group players by school
    for _, row in df.iterrows():
        school_players[row['School']].append(row)

    # Distribute players into groups
    for school, players in school_players.items():
        for i, player in enumerate(players):
            group_index = i % num_groups
            groups[group_index].append(player)

    # Flatten groups into DataFrames
    group_dfs = [pd.DataFrame(group) for group in groups]
    return group_dfs

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
