import subprocess
import os

# Base directory of the scripts to run
base_dir = os.path.join(os.path.dirname(__file__), "..", "src")

# Files in the correct execution order
files_to_run = [
    "data_filtering_and_export.py",
    "group_division_and_allocation.py",
    "group_processing_intermediate.py",
    "bracket_pdf_generator.py"
]

for file in files_to_run:
    file_path = os.path.join(base_dir, file)
    print(f"\n➡️ Running: {file_path}")
    result = subprocess.run(["python", file_path], capture_output=True, text=True)

    if result.stdout:
        print(f"✅ Output:\n{result.stdout}")
    if result.stderr:
        print(f"❌ Errors:\n{result.stderr}")

    print("-" * 60)
