# Marketing Report Generator
![Python](https://img.shields.io/badge/Python-3.12+-blue)
![Status](https://img.shields.io/badge/status-complete-brightgreen)
![License](https://img.shields.io/badge/license-free-lightgrey)

## 📋 Overview

Marketing Report Generator is a Python application that automates the generation of professional marketing campaign reports from CSV data. The tool processes data from multiple campaigns, calculates performance metrics, and exports a formatted Excel report.

## ✨ Features

- **Intuitive GUI**: File and campaign selection through a visual interface with Tkinter
- **Flexible Data Processing**: Support for different CSV structures with configurable column mapping
- **Automatic Metrics Calculation**:
  - Total Spend (BRL)
  - Impressions and Reach
  - Clicks and Conversions
  - Average and Real Cost Per Lead (CPL)
  - New Contacts
- **Professional Reports**: Generation of formatted Excel files with styles, borders, and charts
- **Persistent Configuration**: JSON-based configuration system for reusable mappings

## 🚀 Getting Started

### Prerequisites

- Python 3.7+
- Dependencies: `pandas`, `openpyxl`

### Install Dependencies

```bash
pip install pandas openpyxl
```

### Running the Application

```bash
python main.py
```

### Step-by-Step Guide

1. **Start the Application**: Execute the command above
2. **Select CSV File**: In the file dialog, choose the CSV file containing your marketing data
3. **Confirm Selection**: Confirm that the file is correct
4. **Map Columns**: On first run, configure which column contains campaign names
5. **Configure Metrics**: Select the columns corresponding to each metric (Spend, Impressions, etc.)
6. **Select Campaigns**: Choose which campaigns should be included in the report
7. **Generate Report**: Select the location to save the generated Excel file

## 📁 Project Structure

```
marketing-report/
├── main.py           # Main application with GUI
├── loader.py         # CSV file loading and processing
├── metrics.py        # Marketing metrics calculation
├── reporter.py       # Excel report generation
├── config.py         # Configuration management
├── config.json       # Configuration file (auto-generated)
└── README.md         # This file
```

## 🔧 Configuration

### config.json File

The `config.json` file stores the mapping between CSV columns and marketing metrics. Example:

```json
{
    "spend": "Valor usado (BRL)",
    "impressions": "Impressões",
    "reach": "Alcance",
    "clicks": "Cliques (todos)",
    "conversions": "Conversas por mensagem iniciadas",
    "cost_per_lead": "Custo por conversa por mensagem iniciada",
    "new_contacts": "Custo por novo contato por mensagem"
}
```

You can edit this file directly or let the application configure it automatically on first run.

## 📊 Calculated Metrics

| Metric | Description |
|--------|-------------|
| **Total Spend** | Total amount spent on campaigns (in BRL) |
| **Total Impressions** | Total number of impressions |
| **Total Reach** | Total reach across campaigns |
| **Total Clicks** | Total clicks recorded |
| **Total Conversions** | Total conversions/initiated messages |
| **Avg CPL** | Average cost per lead |
| **Real CPL** | Real cost per conversion (Spend ÷ Conversions) |
| **Total New Contacts** | Total new contacts |

## 📄 Report Format

The generated Excel report includes:

- **Metrics Summary**: Formatted table with all calculated metrics
- **Professional Styling**: Formatting with fonts, colors, and borders
- **Clear Structure**: Data organized by selected campaigns

## 🛠️ Technologies Used

- **Python 3**: Primary language
- **Tkinter**: GUI framework
- **Pandas**: Data processing
- **OpenPyXL**: Excel report generation

## 📝 Usage Example

```python
# The application will guide you through the steps:
# 1. Select your marketing CSV file
# 2. Configure columns (first run)
# 3. Choose desired campaigns
# 4. Save the report in Excel
```

## 🐛 Troubleshooting

### CSV file not found
- Make sure the file is in the correct CSV format
- Check that the file path doesn't contain problematic special characters

### Configuration not loading
- Verify that `config.json` is in the same directory as `main.py`
- Delete the `config.json` file to reconfigure from scratch

### Error generating report
- Verify that the configured columns exist in your CSV
- Confirm that the data in the columns are of the expected type (numeric)

## 📄 License

This project is available for free use.

## 🤝 Contributing

Suggestions and improvements are welcome!

---

**Built with ❤️ to optimize marketing analysis**
