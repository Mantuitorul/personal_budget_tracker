# Personal Budget Tracker

A simple and efficient personal budget tracking system that helps you monitor your income and expenses.

## Features

- Income tracking with categories
- Expense tracking with categories
- Basic analytics and reporting
- Data visualization

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
