# Drawer System

## Project Overview
The Drawer System is a Python-based project designed to streamline the creation of single-elimination draw systems for karate events. It ensures fairness and minimizes bias by automating critical steps such as filtering player data, creating balanced groups, and generating match brackets in a professional format.

## Features

1. **Data Filtering**
   - Filters player data based on gender, attendance day (Saturday or Sunday), belt color, and age group.
   - Outputs structured Excel files for each category in `filtered_data/sat` and `filtered_data/sun` directories.

2. **Group Creation**
   - Sorts players by weight and divides them into balanced groups.
   - Distributes players from the same school evenly across groups.
   - Saves grouped data in the `groups` directory.

3. **Bracket Generation**
   - Generates PDF match brackets using a predefined template (`score_sheet.png`).
   - Randomizes player positions while ensuring logical placement of `BYE` entries.
   - Combines individual PDFs into a consolidated output for each category.

4. **Automation**
   - Automates the entire workflow through the `auto_run.py` script, executing all scripts sequentially.

## Prerequisites

1. **Dependencies**
   - Python 3.8+
   - Required libraries:
     ```bash
     pandas openpyxl reportlab pillow PyPDF2
     ```

2. **Required Files**
   - `Demo_Run.xlsx`: Raw dataset of players.
   - `score_sheet.png`: Template for generating brackets.
   - `Allan-Bold.ttf`: Font file for custom bracket titles.

## Setup Instructions

1. **Clone the Repository**
   ```bash
   git clone https://github.com/ull0sm/Drawer.git
   cd Drawer
   ```

2. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Organize Files**
   - Place the raw dataset (`Demo_Run.xlsx`) and template image (`score_sheet.png`) in the `input_files` directory.

4. **Docker Setup (Optional)**
   - Pull the Docker image:
     ```bash
     docker pull ull0sm/drawer
     ```
   - Run the container:
     ```bash
     docker compose up
     ```

## Directory Structure

```
project_root/
├── src/
│   ├── data_filtering_and_export.py
│   ├── group_division_and_allocation.py
│   ├── group_processing_intermediate.py
│   ├── bracket_pdf_generator.py
├── automation/
│   ├── auto_run.py
├── data/
│   ├── filtered_data/
│   │   ├── sat/
│   │   ├── sun/
│   ├── groups/
│   ├── score_sheets/
│   ├── input_files/
│   │   ├── score_sheet.png
│   │   ├── Demo_Run.xlsx
│   │   ├── Allan-Bold.ttf
│   ├── temp/
├── requirements.txt
├── compose.yaml
├── Dockerfile
```

## Usage

1. **Manual Execution**
   - Run the scripts in the following order:
     ```bash
     python3 src/data_filtering_and_export.py
     python3 src/group_division_and_allocation.py
     python3 src/group_processing_intermediate.py
     python3 src/bracket_pdf_generator.py
     ```

2. **Automated Execution**
   - Run the `auto_run.py` script:
     ```bash
     python3 automation/auto_run.py
     ```

3. **Docker Execution**
   - Start the pipeline in a Docker container:
     ```bash
     docker compose up
     ```

## Outputs

- **Filtered Data**: Organized in `data/filtered_data/sat` and `data/filtered_data/sun`.
- **Grouped Data**: Saved in `data/groups/`.
- **Brackets**: PDF files in `data/score_sheets/`.

## Contributing

1. **Clone the Repository**
   ```bash
   git clone https://github.com/ull0sm/Drawer.git
   cd Drawer
   ```

2. **Create a Feature Branch**
   ```bash
   git checkout -b new-feature
   ```

3. **Implement Changes**
   - Modify the relevant scripts.
   - Test thoroughly.

4. **Commit and Push Changes**
   ```bash
   git add .
   git commit -m "Add [feature description]"
   git push origin new-feature
   ```

5. **Submit a Pull Request**
   - Navigate to the repository on GitHub.
   - Create a pull request from your `new-feature` branch to the `main` branch.

---

For any questions or issues, feel free to open a GitHub issue or contribute to improving the project.

