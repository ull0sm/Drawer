# Drawer

## Project Overview

Drawer is a Python-based project designed to automate the creation of single-elimination draw systems for karate events. The tool ensures fairness and reduces bias by automating the process, which includes filtering player data, creating groups, and generating match brackets in a streamlined and organized way.

## Features

1. **Data Filtering**
   - Filters player data based on gender, day of attendance (Saturday or Sunday), belt color, and age groups.
   - Generates separate Excel files for each filtered category.

2. **Group Creation**
   - Sorts players by weight and divides them into balanced groups.
   - Ensures that players from the same school are distributed evenly across groups.

3. **Bracket Generation**
   - Processes group data and generates PDF brackets using a predefined template.
   - Handles randomization while ensuring proper placement of `BYE` entries.

4. **Automation**
   - Automates the entire pipeline, running all scripts in the correct order to produce the final single-elimination draw system.

## Files and Code Description

### **Code 1:**
This script filters player data from the raw dataset (`Demo_Run.xlsx`) and creates categorized Excel sheets. Key features include:

- Filtering by gender, attendance day, belt color, and age groups.
- Saving the filtered data into structured directories (`filtered_data/sat` and `filtered_data/sun`).

### **Code 2:**
This script creates balanced groups from the filtered datasets. Features include:

- Sorting players by weight.
- Dividing players into groups with a maximum size of 8.
- Ensuring minimal overlap of players from the same school within a group.
- Saving grouped data into Excel files under the `groups` directory.

### **Code 3:**
Acts as a bridge between grouped datasets and the bracket generation algorithm. Features include:

- Reading grouped datasets.
- Configuring categories and gender-based identifiers.
- Preparing data for bracket PDF generation.

### **Code 4:**
This script generates match brackets in PDF format for each group. Features include:

- Using a template (`score_sheet.png`) to structure the brackets.
- Randomizing player positions while maintaining logical placement of `BYE` entries.
- Merging individual PDFs into a single file for each category.

### **Code 5:**
A master script to automate the entire process by executing the other scripts in sequence:

1. `data_filtering_and_export.py`
2. `group_division_and_allocation.py`
3. `group_processing_intermediate.py`
4. `bracket_pdf_generator.py`

## Prerequisites

- Python 3.8+
- Required Python libraries:
  - `pandas`
  - `openpyxl`
  - `reportlab`
  - `pillow`
  - `PyPDF2`
- Raw dataset: `Demo_Run.xlsx`
- Template image: `score_sheet.png`

## Setup Instructions

1. Clone the repository to your local machine:
   ```bash
   git clone https://github.com/ull0sm/Drawer.git
   cd Drawer
   ```

2. Install the required libraries:
   ```bash
   pip install pandas openpyxl reportlab pillow PyPDF2
   ```

3. Place the raw dataset (`Demo_Run.xlsx`) in the root directory.
4. Place the template image (`score_sheet.png`) in the root directory.

## Usage

1. To manually execute each step, run the scripts in the following order:
   ```bash
   python data_filtering_and_export.py
   python group_division_and_allocation.py
   python group_processing_intermediate.py
   python bracket_pdf_generator.py
   ```

2. To automate the process, run `auto_run.py`:
   ```bash
   python auto_run.py
   ```

## Output

- Filtered data files in `filtered_data/sat` and `filtered_data/sun`.
- Grouped data files in the `groups` directory.
- PDF match brackets in the `score_sheets` directory.

## Directory Structure

```
project_root/
├── data_filtering_and_export.py
├── group_division_and_allocation.py
├── group_processing_intermediate.py
├── bracket_pdf_generator.py
├── auto_run.py
├── Demo_Run.xlsx
├── score_sheet.png
├── filtered_data/
│   ├── sat/
│   ├── sun/
├── groups/
├── score_sheets/
```

## Contributing

### Cloning the Repository and Creating a Feature Branch

1. Clone the repository to your local machine:
   ```bash
   git clone https://github.com/ull0sm/Drawer.git
   cd Drawer
   ```

2. Create a new branch for your feature:
   ```bash
   git checkout -b new-feature
   ```

### Making Changes

1. Implement your changes in the relevant files.
2. Test your changes to ensure they work as expected.

### Committing and Pushing Changes

1. Add your changes to the staging area:
   ```bash
   git add .
   ```

2. Commit your changes with a descriptive message:
   ```bash
   git commit -m "Add [feature description]"
   ```

3. Push your changes to the remote repository:
   ```bash
   git push origin new-feature
   ```

### Creating a Pull Request

1. Navigate to the repository on GitHub.
2. Go to the "Pull Requests" tab and click "New Pull Request."
3. Select your `new-feature` branch and compare it with the `main` branch.
4. Add a title and description for your pull request.
5. Submit the pull request for review.
