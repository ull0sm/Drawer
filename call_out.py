import os
import pandas as pd
from part1 import read, pdf_merger
import part1

def process_datasets_in_groups(folder_path):
    # Ensure the folder exists
    if not os.path.exists(folder_path):
        print(f"Folder {folder_path} does not exist!")
        return
    
    # Loop through all files in the folder
    for filename in os.listdir(folder_path):
        # Only process Excel files
        if filename.endswith(".xlsx"):
            datasetname = filename.split('.')[0]  # Remove the file extension
            datasetpath = os.path.join(folder_path, filename)
            
            # Extract SEX from the filename
            if 'M' in filename:
                SEX_value = 1405
            else:
                SEX_value = 1320

            # Import part1 and set category and SEX
            part1.category = datasetname
            part1.SEX = SEX_value
            
            print(f"Processing {filename} with category {datasetname} and SEX {SEX_value}")

            # Now read the dataset and create the necessary PDFs
            read(datasetpath)  # This reads the dataset
            pdf_merger()  # This merges the PDFs

# Example usage
folder_path = ".\\groups"
process_datasets_in_groups(folder_path)