# src/database/database_manager.py
from typing import Optional
import sqlite3
from datetime import datetime
from pathlib import Path

class DatabaseManager:
    def __init__(self, db_path: Optional[str] = None):
        if db_path is None:
            db_path = Path("data/budget.db")
        
        # Ensure the data directory exists
        db_path.parent.mkdir(parents=True, exist_ok=True)
        
        self.db_path = db_path
        self._init_database()

    def _init_database(self) -> None:
        """Initialize the database with required tables"""
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            
            # Create income entries table
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS income_entries (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    amount REAL NOT NULL,
                    source TEXT NOT NULL,
                    date TIMESTAMP NOT NULL,
                    category TEXT NOT NULL,
                    description TEXT
                )
            ''')
            
            # Create expense entries table
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS expense_entries (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    amount REAL NOT NULL,
                    vendor TEXT NOT NULL,
                    date TIMESTAMP NOT NULL,
                    category TEXT NOT NULL,
                    description TEXT
                )
            ''')
            
            # Create custom income categories table
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS custom_income_categories (
                    name TEXT PRIMARY KEY,
                    description TEXT NOT NULL
                )
            ''')
            
            # Create custom expense categories table
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS custom_expense_categories (
                    name TEXT PRIMARY KEY,
                    description TEXT NOT NULL
                )
            ''')
            
            conn.commit()

    def add_income_entry(self, entry_data: dict) -> int:
        """Add a new income entry to the database"""
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute('''
                INSERT INTO income_entries (amount, source, date, category, description)
                VALUES (?, ?, ?, ?, ?)
            ''', (
                entry_data['amount'],
                entry_data['source'],
                entry_data['date'],
                entry_data['category'],
                entry_data.get('description', '')
            ))
            conn.commit()
            return cursor.lastrowid

    def add_expense_entry(self, entry_data: dict) -> int:
        """Add a new expense entry to the database"""
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute('''
                INSERT INTO expense_entries (amount, vendor, date, category, description)
                VALUES (?, ?, ?, ?, ?)
            ''', (
                entry_data['amount'],
                entry_data['vendor'],
                entry_data['date'],
                entry_data['category'],
                entry_data.get('description', '')
            ))
            conn.commit()
            return cursor.lastrowid

    def get_all_income_entries(self) -> list:
        """Retrieve all income entries from the database"""
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute('SELECT * FROM income_entries ORDER BY date DESC')
            return cursor.fetchall()

    def get_all_expense_entries(self) -> list:
        """Retrieve all expense entries from the database"""
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute('SELECT * FROM expense_entries ORDER BY date DESC')
            return cursor.fetchall()

    def add_custom_income_category(self, name: str, description: str) -> bool:
        """Add a new custom income category"""
        try:
            with sqlite3.connect(self.db_path) as conn:
                cursor = conn.cursor()
                cursor.execute('''
                    INSERT INTO custom_income_categories (name, description)
                    VALUES (?, ?)
                ''', (name.upper(), description))
                conn.commit()
                return True
        except sqlite3.IntegrityError:
            return False

    def add_custom_expense_category(self, name: str, description: str) -> bool:
        """Add a new custom expense category"""
        try:
            with sqlite3.connect(self.db_path) as conn:
                cursor = conn.cursor()
                cursor.execute('''
                    INSERT INTO custom_expense_categories (name, description)
                    VALUES (?, ?)
                ''', (name.upper(), description))
                conn.commit()
                return True
        except sqlite3.IntegrityError:
            return False

    def get_custom_income_categories(self) -> dict:
        """Retrieve all custom income categories"""
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute('SELECT name, description FROM custom_income_categories')
            return dict(cursor.fetchall())

    def get_custom_expense_categories(self) -> dict:
        """Retrieve all custom expense categories"""
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute('SELECT name, description FROM custom_expense_categories')
            return dict(cursor.fetchall())