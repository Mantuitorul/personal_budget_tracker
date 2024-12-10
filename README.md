# Personal Budget Tracker

## Table of Contents
1. [Overview](#overview)
2. [Features](#features)
3. [Database Structure](#database-structure)
4. [Settings Configuration](#settings-configuration)
5. [Setup Instructions](#setup-instructions)
6. [Usage Guide](#usage-guide)
   - [Managing Income](#managing-income)
   - [Managing Expenses](#managing-expenses)
   - [Viewing Reports](#viewing-reports)
   - [Exporting Data](#exporting-data)
7. [Available Categories](#available-categories)
8. [Dependencies](#dependencies)

## Overview
A command-line application for personal finance management that helps users track their income and expenses, categorize transactions, and generate financial reports. This tool is designed to provide a simple yet effective way to maintain control over your personal finances.

## Features
- Income management with customizable categories (salary, freelance, investments, etc.)
- Expense tracking with predefined and custom categories
- Database persistence using SQLite
- Category-based financial analysis
- Budget summaries and reporting
- CSV and Excel export functionality for financial reports
- Custom category creation for both income and expenses
- Monthly trend analysis and financial summaries

## Database Structure
The application uses SQLite with four main tables:
- `income_entries`: Stores all income transactions
- `expense_entries`: Stores all expense transactions
- `custom_income_categories`: Stores user-defined income categories
- `custom_expense_categories`: Stores user-defined expense categories

Database location: `data/budget.db` (created automatically)

## Settings Configuration
The application requires a `settings.py` file for configuration. Copy `example_settings.py` and modify as needed:

```python
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
DATABASE = {
    'path': BASE_DIR / 'data' / 'budget.db'
}
DEBUG = True
VERSION = '1.0.0'
```

## Setup Instructions
1. Clone the repository:
   ```bash
   git clone https://github.com/Mantuitorul/personal_budget_tracker
   cd personal_budget_tracker
   ```

2. Create a virtual environment:
   ```bash
   python -m venv .venv
   ```

3. Activate the virtual environment:
   - Windows:
     ```bash
     .venv\Scripts\activate
     ```
   - macOS/Linux:
     ```bash
     source .venv/bin/activate
     ```

4. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

5. Create your settings file:
   - Copy `example_settings.py` to `settings.py`
   - Update the database configurations in `settings.py`

6. Initialize the database:
   ```bash
   python main.py --init-db
   ```

7. Run the application:
   ```bash
   python main.py
   ```

## Usage Guide

### Managing Income
The application allows you to track various types of income:

```python
# Adding a regular income entry
income_manager.add_income(
    amount=3000.0,
    source="Tech Corp",
    category="SALARY",
    description="Monthly salary"
)

# Adding a custom income category
income_manager.add_custom_category("YOUTUBE", "Income from YouTube channel")

# Adding income with custom category
income_manager.add_income(
    amount=200.0,
    source="YouTube",
    category="YOUTUBE",
    description="Ad revenue"
)
```

### Managing Expenses
Track your expenses with predefined or custom categories:

```python
# Adding a regular expense
expense_manager.add_expense(
    amount=1200.0,
    vendor="ABC Apartments",
    category="HOUSING",
    description="Monthly rent"
)

# Adding a custom expense category
expense_manager.add_custom_category("PETS", "Pet-related expenses")

# Adding expense with custom category
expense_manager.add_expense(
    amount=100.0,
    vendor="Pet Store",
    category="PETS",
    description="Dog food and supplies"
)
```

### Viewing Reports
The application provides several ways to view your financial data:

1. View Income Summary:
   ```python
   income_manager.get_category_summary()
   ```

2. View Expense Summary:
   ```python
   expense_manager.get_category_summary()
   ```

3. View Budget Analysis:
   ```python
   analyzer.get_monthly_summary(year, month)
   analyzer.get_category_analysis(year, month)
   analyzer.get_trend_analysis(months=6)
   ```

### Exporting Data
Export your financial data in CSV or Excel format:

```python
# Export monthly report to CSV
analyzer.export_monthly_report_to_csv(year, month)

# Export monthly report to Excel
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
- python-dotenv
- SQLAlchemy
- pandas
- matplotlib
- openpyxl

See `requirements.txt` for a complete list of dependencies.