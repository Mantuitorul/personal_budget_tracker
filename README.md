# Personal Budget Tracker

A simple and efficient personal budget tracking system that helps you monitor your income and expenses.

## Features

- Income management with customizable categories (salary, freelance, investments, etc.)
- Expense tracking with predefined and custom categories
- Database persistence using SQLite
- Category-based financial analysis
- Budget summaries and reporting
- CSV export functionality for financial reports

## Database Structure

The application uses SQLite with four main tables:
- income_entries: Stores all income transactions
- expense_entries: Stores all expense transactions
- custom_income_categories: Stores user-defined income categories
- custom_expense_categories: Stores user-defined expense categories

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

6. Create a `.env` file:
   - Copy `.env.example` to `.env`
   - Update the environment variables as needed

7. Initialize the database:
   ```bash
   python main.py --init-db
   ```

8. Run the application:
   ```bash
   python main.py
   ```

## Dependencies

See `requirements.txt` for a full list of dependencies.
