# 🚀 Getting Started with Drawer System

Get up and running with the Karate Tournament Drawer System.

## 📋 Prerequisites

### System Requirements
- **Python:** 3.8 or higher
- **Operating System:** Windows, macOS, or Linux
- **Memory:** Minimum 512MB RAM (recommended: 1GB+)
- **Storage:** 100MB free space for installation + space for tournament data

### Required Python Libraries
The following packages will be installed via `requirements.txt`:
- `pandas` (Data manipulation and analysis)
- `openpyxl` (Excel file handling)
- `reportlab` (PDF generation)
- `pillow` (Image processing)
- `PyPDF2` (PDF manipulation)

### Input Files Needed
Ensure these files are placed in the `data/input_files/` directory:

| File | Purpose | Format |
|------|---------|--------|
| `Demo_Run.xlsx` | Raw player dataset | Excel spreadsheet with columns: NAME, SEX, DAY, BELT, AGE, WEIGHT, SCHOOL |
| `score_sheet.png` | Tournament bracket template | PNG image file |
| `Allan-Bold.ttf` | Custom font for bracket titles | TrueType font file |

## 🛠️ Installation

### Option 1: Standard Installation
1. **Clone the Repository**
   ```bash
   git clone https://github.com/ull0sm/Drawer.git
   cd Drawer
   ```
2. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```
3. **Prepare Input Files**
   - Place your tournament data (`Demo_Run.xlsx`) in `data/input_files/`
   - Ensure the bracket template (`score_sheet.png`) and font (`Allan-Bold.ttf`) are in `data/input_files/`

### Option 2: Docker Installation
1. **Pull the Docker Image**
   ```bash
   docker pull ull0sm/drawer
   ```
2. **Run with Docker Compose**
   ```bash
   docker compose up
   ```
   This will automatically mount the output directories to your local machine at `~/Desktop/output/`.

## 🎯 Usage

### Automated Execution (Recommended)
Run the entire tournament preparation pipeline:
```bash
python automation/auto_run.py
```

### Manual Step-by-Step Execution
For debugging or custom workflows, run scripts individually:
```bash
# Step 1: Filter
python src/data_filtering_and_export.py
# Step 2: Group
python src/group_division_and_allocation.py
# Step 3: Process
python src/group_processing_intermediate.py
# Step 4: Generate
python src/bracket_pdf_generator.py
```

## 📤 Outputs
After execution, results are organized in:
- `data/filtered_data/`: Player lists by category
- `data/groups/`: Balanced athlete groups
- `data/score_sheets/`: Final PDF tournament brackets

## 🐳 Docker Usage
The `compose.yaml` automatically mounts output directories:
- Container path: `/app/data/groups` → Local: `~/Desktop/output/data/groups`
- Container path: `/app/data/score_sheets` → Local: `~/Desktop/output/data/score_sheets`

## 🔧 Troubleshooting

### Common Issues
- **`FileNotFoundError: Demo_Run.xlsx`**: Check if it's in `data/input_files/`
- **`ModuleNotFoundError: No module named 'pandas'`**: Run `pip install -r requirements.txt`
- **`Font not found: Allan-Bold.ttf`**: Check `data/input_files/`
- **Permission Denied**: Run terminal as Administrator (Windows) or use `chmod 755 data/` (Linux)
