# Personal Budget Tracker

## Table of Contents
1. [Overview](#overview)
2. [Features](#features)
3. [Project Structure](#project-structure)
4. [Database Structure](#database-structure)
5. [Settings Configuration](#settings-configuration)
6. [Setup Instructions](#setup-instructions)
7. [Usage Guide](#usage-guide)
   - [Managing Income](#managing-income)
   - [Managing Expenses](#managing-expenses)
   - [Viewing Reports](#viewing-reports)
   - [Exporting Data](#exporting-data)
8. [Available Categories](#available-categories)
9. [Dependencies](#dependencies)

## Overview
A command-line application for personal finance management that helps users track their income and expenses, categorize transactions, and generate financial reports. This tool is designed to provide a simple yet effective way to maintain control over your personal finances.

## Features
- Income management with customizable categories
- Expense tracking with predefined and custom categories
- Database persistence using SQLite
- Category-based financial analysis
- Budget summaries and reporting
- CSV and Excel export functionality for financial reports
- Custom category creation for both income and expenses

## Project Structure
```
personal_budget_tracker/
│   .gitignore
│   main.py
│   README.md
│   requirements.txt
│   sample_budget.db
│
├───data/               # Database storage
│       budget.db
│
├───reports/           # Generated reports
│       budget_report_*.csv
│       budget_report_*.xlsx
│
└───src/
    │   example_settings.py
    │   settings.py    # Created from example_settings.py
    │   __init__.py
    │
    ├───analytics/     # Analysis and reporting
    ├───database/      # Database management
    ├───expenses/      # Expense tracking
    ├───income/        # Income tracking
    └───ui/           # User interface
```

## Database Structure
The application uses SQLite with four main tables:
- `income_entries`: Stores all income transactions
- `expense_entries`: Stores all expense transactions
- `custom_income_categories`: Stores user-defined income categories
- `custom_expense_categories`: Stores user-defined expense categories

Location: `data/budget.db` (created automatically on first run)

## Settings Configuration
1. The application requires a `settings.py` file in the `src` directory
2. Copy `src/example_settings.py` to `src/settings.py` and modify as needed:

```python
from pathlib import Path

# Base directory of the project
BASE_DIR = Path(__file__).resolve().parent.parent

# Database settings
DATABASE = {
    'path': BASE_DIR / 'data' / 'budget.db'
}

# Application settings
DEBUG = True
VERSION = '1.0.0'
```

## Setup Instructions
1. Clone the repository:
   ```bash
   git clone https://github.com/Mantuitorul/personal_budget_tracker
   cd personal_budget_tracker
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv .venv
   
   # Windows:
   .venv\Scripts\activate
   
   # macOS/Linux:
   source .venv/bin/activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Configure settings:
   - Copy `src/example_settings.py` to `src/settings.py`
   - Update configurations if needed (database path, debug mode)

5. Initialize the database:
   ```bash
   python main.py --init-db
   ```

6. Run the application:
   ```bash
   python main.py
   ```

> A `sample_budget.db` has been provided in the repo. You can use that with the `sample_settings.py` (don't forget to rename them to `settings.py` in the `/src`). All you need to do is to copy `sample_budget.db` to data folder in the root directory and rename it to `budget.db`. This should work if you didn't make any modifications to `settings.py` provided.

## Usage Guide

### Managing Income
```python
# Adding income entry
income_manager.add_income(
    amount=3000.0,
    source="Tech Corp",
    category="SALARY",
    description="Monthly salary"
)

# Adding custom income category
income_manager.add_custom_category("YOUTUBE", "Income from YouTube channel")
```

### Managing Expenses
```python
# Adding expense
expense_manager.add_expense(
    amount=1200.0,
    vendor="ABC Apartments",
    category="HOUSING",
    description="Monthly rent"
)

# Adding custom expense category
expense_manager.add_custom_category("PETS", "Pet-related expenses")
```

### Viewing Reports
```python
# View category summaries
income_manager.get_category_summary()
expense_manager.get_category_summary()

# View detailed analysis
analyzer.get_monthly_summary(year, month)
analyzer.get_category_analysis(year, month)
analyzer.get_trend_analysis(months=6)
```

### Exporting Data
Reports are automatically saved in the reports/ directory (created automatically if it doesn't exist):
```python
# Export monthly reports
analyzer.export_monthly_report_to_csv(year, month)
analyzer.export_monthly_report_to_excel(year, month)
```

## Available Categories

### Default Income Categories
- SALARY: Regular employment income
- FREELANCE: Independent contractor work
- INVESTMENTS: Investment returns
- RENTAL: Rental property income
- BUSINESS: Business income
- GIFTS: Monetary gifts received
- OTHERS: Miscellaneous income

### Default Expense Categories
- HOUSING: Rent, mortgage, utilities
- FOOD: Groceries and dining
- TRANSPORTATION: Fuel, public transit, maintenance
- HEALTHCARE: Medical expenses
- ENTERTAINMENT: Recreation and leisure
- SHOPPING: Clothing, electronics
- EDUCATION: Training and education
- UTILITIES: Electricity, water, internet
- INSURANCE: Insurance premiums
- DEBT: Debt payments
- SAVINGS: Savings and investments
- OTHERS: Miscellaneous expenses

## Dependencies
Key dependencies include:
- SQLAlchemy: Database ORM
- pandas: Data analysis and Excel export
- matplotlib: Visualization
- openpyxl: Excel file handling

For a complete list of dependencies, see `requirements.txt`.
