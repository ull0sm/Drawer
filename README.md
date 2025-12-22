# 🥋 Drawer System

[![Python](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![Docker](https://img.shields.io/badge/docker-supported-blue.svg)](https://www.docker.com/)

> **A comprehensive Python-based tournament draw system for karate events**

The Drawer System automates the creation of fair and unbiased single-elimination tournament brackets for karate competitions. It streamlines the entire process from data filtering to bracket generation, ensuring professional-quality tournament organization.

## 📋 Table of Contents

- [🚀 Quick Start](#-quick-start)
- [✨ Features](#-features)
- [📋 Prerequisites](#-prerequisites)
- [🛠️ Installation](#️-installation)
- [📁 Directory Structure](#-directory-structure)
- [🎯 Usage](#-usage)
- [📤 Outputs](#-outputs)
- [🐳 Docker Usage](#-docker-usage)
- [🔧 Troubleshooting](#-troubleshooting)
- [🤝 Contributing](#-contributing)

## 🚀 Quick Start

Get up and running in 3 steps:

1. **Clone and install:**
   ```bash
   git clone https://github.com/ull0sm/Drawer.git
   cd Drawer
   pip install -r requirements.txt
   ```

2. **Prepare your data:**
   - Place your player data Excel file (`Demo_Run.xlsx`) in `data/input_files/`
   - Ensure `score_sheet.png` template is in `data/input_files/`

3. **Run the system:**
   ```bash
   python automation/auto_run.py
   ```

Your tournament brackets will be generated in `data/score_sheets/`! 🎉

## ✨ Features

### 🔍 **Intelligent Data Filtering**
- Filters player data by gender, attendance day (Saturday/Sunday), belt color, and age group
- Generates organized Excel files in category-specific directories
- Handles multiple belt levels (White, Yellow, Blue, Purple, Green, Brown, Black)

### 👥 **Smart Group Creation**  
- Sorts players by weight for balanced competition
- Distributes players from the same school evenly across groups
- Prevents unfair advantages through intelligent allocation algorithms

### 📄 **Professional Bracket Generation**
- Creates PDF tournament brackets using customizable templates
- Randomizes player positions while maintaining logical `BYE` placement
- Combines individual category PDFs into consolidated tournament documents

### ⚡ **Complete Automation**
- One-click execution through `auto_run.py` automation script
- Sequential processing of all tournament preparation steps
- Error handling and progress tracking throughout the pipeline

## 📋 Prerequisites

### System Requirements
- **Python:** 3.8 or higher
- **Operating System:** Windows, macOS, or Linux
- **Memory:** Minimum 512MB RAM (recommended: 1GB+)
- **Storage:** 100MB free space for installation + space for tournament data

### Required Python Libraries
The following packages will be installed via `requirements.txt`:
```
pandas      # Data manipulation and analysis
openpyxl    # Excel file handling
reportlab   # PDF generation
pillow      # Image processing
PyPDF2      # PDF manipulation
```

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
   - Ensure the bracket template (`score_sheet.png`) is in `data/input_files/`
   - Verify the font file (`Allan-Bold.ttf`) is in `data/input_files/`

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

## 📁 Directory Structure

```
Drawer/
├── 📁 src/                              # Core application scripts
│   ├── 🐍 data_filtering_and_export.py      # Step 1: Filter and categorize players
│   ├── 🐍 group_division_and_allocation.py  # Step 2: Create balanced groups
│   ├── 🐍 group_processing_intermediate.py  # Step 3: Process group data
│   └── 🐍 bracket_pdf_generator.py          # Step 4: Generate PDF brackets
├── 📁 automation/
│   └── 🐍 auto_run.py                       # Main automation script
├── 📁 data/                             # Data directories (auto-created)
│   ├── 📁 input_files/                      # Input files location
│   │   ├── 📄 Demo_Run.xlsx                 # Tournament player data
│   │   ├── 🖼️ score_sheet.png               # Bracket template
│   │   └── 🔤 Allan-Bold.ttf                # Custom font
│   ├── 📁 filtered_data/                   # Filtered results by category
│   │   ├── 📁 sat/                          # Saturday categories
│   │   └── 📁 sun/                          # Sunday categories  
│   ├── 📁 groups/                           # Grouped player data
│   ├── 📁 score_sheets/                     # Generated PDF brackets
│   └── 📁 temp/                             # Temporary processing files
├── 📄 requirements.txt                  # Python dependencies
├── 🐳 compose.yaml                      # Docker Compose configuration
├── 🐳 Dockerfile                        # Docker image definition
└── 📖 README.md                         # This documentation
```

## 🎯 Usage

### Automated Execution (Recommended)

The simplest way to run the entire tournament preparation pipeline:

```bash
python automation/auto_run.py
```

This executes all four processing steps automatically with progress tracking and error reporting.

### Manual Step-by-Step Execution

For debugging or custom workflows, run scripts individually:

```bash
# Step 1: Filter and categorize player data
python src/data_filtering_and_export.py

# Step 2: Create balanced groups by weight and school
python src/group_division_and_allocation.py  

# Step 3: Process and prepare group data
python src/group_processing_intermediate.py

# Step 4: Generate PDF tournament brackets
python src/bracket_pdf_generator.py
```

### Processing Workflow

1. **Data Filtering** → Categorizes players by gender, day, belt, and age
2. **Group Division** → Creates weight-balanced groups with school distribution  
3. **Group Processing** → Prepares data for bracket generation
4. **Bracket Generation** → Creates final PDF tournament brackets

## 📤 Outputs

After successful execution, you'll find organized tournament data in these locations:

### 📊 Filtered Data
- **Location:** `data/filtered_data/`
- **Structure:** 
  - `sat/` - Saturday tournament categories
  - `sun/` - Sunday tournament categories
- **Format:** Excel files (.xlsx) organized by gender, belt, and age group

### 👥 Grouped Data  
- **Location:** `data/groups/`
- **Content:** Player groups balanced by weight and school distribution
- **Format:** Excel files ready for bracket generation

### 🏆 Tournament Brackets
- **Location:** `data/score_sheets/`
- **Content:** Professional PDF tournament brackets
- **Features:** 
  - Randomized player placement
  - Proper BYE positioning
  - Consolidated category documents
  - Print-ready format

## 🐳 Docker Usage

### Quick Start with Docker

```bash
# Pull and run the container
docker pull ull0sm/drawer
docker compose up
```

### Docker Configuration

The `compose.yaml` automatically mounts output directories:
- Container path: `/app/data/groups` → Local path: `~/Desktop/output/data/groups`
- Container path: `/app/data/score_sheets` → Local path: `~/Desktop/output/data/score_sheets`

### Custom Docker Setup

```bash
# Build your own image
docker build -t my-drawer .

# Run with custom volume mounts
docker run -v $(pwd)/data:/app/data my-drawer
```

## 🔧 Troubleshooting

### Common Issues and Solutions

#### ❌ `FileNotFoundError: Demo_Run.xlsx not found`
**Solution:** Ensure your input Excel file is in `data/input_files/Demo_Run.xlsx`

#### ❌ `ModuleNotFoundError: No module named 'pandas'`
**Solution:** Install dependencies: `pip install -r requirements.txt`

#### ❌ `Permission denied when writing files`
**Solution:** 
- Check directory permissions: `chmod 755 data/`
- Run with appropriate user permissions
- On Windows, run terminal as Administrator

#### ❌ `Empty or malformed output files`
**Solutions:**
- Verify input Excel file has required columns: NAME, SEX, DAY, BELT, AGE, WEIGHT, SCHOOL
- Check that player data contains valid values (no empty cells in critical columns)
- Ensure age and weight values are numeric

#### ❌ `Font not found: Allan-Bold.ttf`
**Solution:** Place the font file in `data/input_files/Allan-Bold.ttf`

#### ❌ `Docker container exits immediately`
**Solutions:**
- Check Docker logs: `docker logs <container_id>`
- Verify volume mounts exist: `mkdir -p ~/Desktop/output/data/{groups,score_sheets}`
- Ensure input files are properly mounted

### Getting Help

1. **Check the console output** - The automation script provides detailed progress and error messages
2. **Verify input data format** - Ensure your Excel file matches the expected column structure  
3. **Run scripts individually** - Use manual execution to isolate issues
4. **Check file permissions** - Ensure the application can read/write in the data directories

## 🤝 Contributing

We welcome contributions to improve the Drawer System! Here's how you can help:

### 🚀 Getting Started

1. **Fork and Clone**
   ```bash
   git clone https://github.com/ull0sm/Drawer.git
   cd Drawer
   ```

2. **Set Up Development Environment**
   ```bash
   pip install -r requirements.txt
   python automation/auto_run.py  # Test the system works
   ```

3. **Create a Feature Branch**
   ```bash
   git checkout -b feature/your-feature-name
   ```

### 🔧 Development Guidelines

- **Code Style:** Follow PEP 8 Python style guidelines
- **Testing:** Test your changes with sample tournament data
- **Documentation:** Update README.md if you change functionality
- **Commits:** Use clear, descriptive commit messages

### 🎯 Areas for Contribution

- **🐛 Bug Fixes:** Report and fix issues
- **✨ New Features:** Additional tournament formats, export options
- **📖 Documentation:** Improve guides and examples  
- **🧪 Testing:** Add automated tests
- **🎨 Templates:** New bracket designs and layouts
- **🌐 Internationalization:** Multi-language support

### 📤 Submitting Changes

1. **Commit Your Changes**
   ```bash
   git add .
   git commit -m "feat: add new bracket template design"
   ```

2. **Push and Create PR**
   ```bash
   git push origin feature/your-feature-name
   ```
   
3. **Open a Pull Request** on GitHub with:
   - Clear description of changes
   - Screenshots (if UI changes)
   - Test results with sample data

### 📋 Issue Reporting

Found a bug? Have a feature request? [Open an issue](https://github.com/ull0sm/Drawer/issues) and include:

- **Environment:** OS, Python version, installation method
- **Steps to Reproduce:** Clear reproduction steps
- **Expected vs Actual:** What should happen vs what happens
- **Sample Data:** Anonymized tournament data (if relevant)

---

## 🙏 Acknowledgments

- Built for karate tournament organizers worldwide
- Inspired by the need for fair and unbiased tournament draws
- Thanks to all contributors who help improve the system

---

**Made with ❤️ for the karate community**

For questions, issues, or contributions, visit the [GitHub repository](https://github.com/ull0sm/Drawer) or open an issue.

