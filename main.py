#!/usr/bin/env python3
import sys
import os
from pathlib import Path
sys.path.append(str(Path(__file__).parent))

from pathlib import Path
import argparse
from src.database import DatabaseManager
from src.income import IncomeManager
from src.expenses import ExpenseManager
from src.ui import run_cli 

def main():
    # Ensure correct working directory, changes the working directory to where main.py is located
    os.chdir(Path(__file__).parent)

    parser = argparse.ArgumentParser(description='Personal Budget Tracker')
    parser.add_argument('--init-db', action='store_true', help='Initialize the database')
    args = parser.parse_args()

    try:
        db_manager = DatabaseManager()
        
        if args.init_db:
            print("Database initialized successfully!")
            return

        run_cli(db_manager)
    except Exception as e:
        print(f"Error: {str(e)}")
        return 1

if __name__ == "__main__":
    main()