import subprocess
import os

def run_script(script_name):
    try:
        # Run the script as a subprocess
        print(f"Running {script_name}...")
        subprocess.run(["python", script_name], check=True)
        print(f"{script_name} completed successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Error occurred while running {script_name}: {e}")
        raise

def main():
    # Define the scripts in order
    scripts = [
        "data_filtering_and_export.py",
        "group_division_and_allocation.py",
        "group_processing_intermediate.py",
        "bracket_pdf_generator.py"
    ]

    # Run each script in order
    for script in scripts:
        run_script(script)

    print("All steps completed successfully.")

if __name__ == "__main__":
    main()