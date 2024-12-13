# src/expenses/expense_manager.py
from datetime import datetime
from typing import List, Optional, Dict
from .expense_entry import ExpenseEntry
from .expense_categories import ExpenseCategoryManager

class ExpenseManager:
    def __init__(self, db_connection):
        self.db_connection = db_connection
        self.category_manager = ExpenseCategoryManager()
        self.expense_entries = []
        
        # Load custom categories from database
        custom_categories = self.db_connection.get_custom_expense_categories()
        for name, description in custom_categories.items():
            self.category_manager._custom_categories[name] = description
        self._load_entries_from_db()

    def _load_entries_from_db(self):
        db_entries = self.db_connection.get_all_expense_entries()
        for entry in db_entries:
            self.expense_entries.append(ExpenseEntry(
                amount=entry[1],
                vendor=entry[2],
                date=datetime.strptime(entry[3], '%Y-%m-%d %H:%M:%S'),
                category=entry[4],
                description=entry[5]
            ))

    def add_expense(self, amount: float, vendor: str, category: str, 
                   description: str = "", date: Optional[datetime] = None) -> Optional[ExpenseEntry]:
        if not self.category_manager.is_valid_category(category):
            print(f"Error: Invalid category '{category}'. Valid categories are: {self.get_available_categories()}")
            return None

        if date is None:
            date = datetime.now()
            
        entry = ExpenseEntry(amount, vendor, date, category.upper(), description)
        entry_data = entry.to_dict()
        self.db_connection.add_expense_entry(entry_data)
        self.expense_entries.append(entry)
        return entry

    def get_available_categories(self) -> Dict[str, str]:
        return self.category_manager.get_all_categories()

    def add_custom_category(self, name: str, description: str) -> bool:
        if self.db_connection.add_custom_expense_category(name, description):
            return self.category_manager.add_custom_category(name, description)
        return False

    def get_expenses_by_category(self, category: str) -> List[ExpenseEntry]:
        if not self.category_manager.is_valid_category(category):
            print(f"Warning: Invalid category '{category}'")
            return []
        return [entry for entry in self.expense_entries if entry.category.upper() == category.upper()]

    def get_category_summary(self) -> Dict[str, float]:
        summary = {}
        for entry in self.expense_entries:
            category = entry.category.upper()
            summary[category] = summary.get(category, 0) + entry.amount
        return summary

    def get_all_expenses(self) -> List[ExpenseEntry]:
        return self.expense_entries

    def calculate_total_expenses(self) -> float:
        return sum(entry.amount for entry in self.expense_entries)