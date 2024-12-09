# src/expenses/expense_manager.py
from datetime import datetime
from typing import List, Optional, Dict
from .expense_entry import ExpenseEntry
from .expense_categories import ExpenseCategoryManager

class ExpenseManager:
    def __init__(self, db_connection=None):
        self.expense_entries: List[ExpenseEntry] = []
        self.db_connection = db_connection
        self.category_manager = ExpenseCategoryManager()

    def add_expense(self, amount: float, vendor: str, category: str, 
                   description: str = "", date: Optional[datetime] = None) -> Optional[ExpenseEntry]:
        """Add a new expense entry with category validation"""
        if not self.category_manager.is_valid_category(category):
            print(f"Error: Invalid category '{category}'. Valid categories are: {self.get_available_categories()}")
            return None

        if date is None:
            date = datetime.now()
            
        entry = ExpenseEntry(
            amount=amount,
            vendor=vendor,
            date=date,
            category=category.upper(),
            description=description
        )
        
        self.expense_entries.append(entry)
        self._save_to_db(entry)
        return entry

    def get_available_categories(self) -> Dict[str, str]:
        """Get all available expense categories"""
        return self.category_manager.get_all_categories()

    def add_custom_category(self, name: str, description: str) -> bool:
        """Add a new custom expense category"""
        return self.category_manager.add_custom_category(name, description)

    def get_expenses_by_category(self, category: str) -> List[ExpenseEntry]:
        """Filter expense entries by category"""
        if not self.category_manager.is_valid_category(category):
            print(f"Warning: Invalid category '{category}'")
            return []
        return [entry for entry in self.expense_entries if entry.category.upper() == category.upper()]

    def get_category_summary(self) -> Dict[str, float]:
        """Get total expenses by category"""
        summary = {}
        for entry in self.expense_entries:
            category = entry.category.upper()
            summary[category] = summary.get(category, 0) + entry.amount
        return summary

    def get_all_expenses(self) -> List[ExpenseEntry]:
        """Retrieve all expense entries"""
        return self.expense_entries

    def calculate_total_expenses(self) -> float:
        """Calculate total expenses from all entries"""
        return sum(entry.amount for entry in self.expense_entries)

    def _save_to_db(self, entry: ExpenseEntry) -> None:
        """Save expense entry to database"""
        if self.db_connection is not None:
            # Implementation will depend on your database module
            pass