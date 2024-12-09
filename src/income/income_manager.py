from datetime import datetime
from typing import List, Optional, Dict
from .income_entry import IncomeEntry
from .income_categories import IncomeCategoryManager, IncomeCategory

class IncomeManager:
    def __init__(self, db_connection=None):
        self.income_entries: List[IncomeEntry] = []
        self.db_connection = db_connection
        self.category_manager = IncomeCategoryManager()

    def add_income(self, amount: float, source: str, category: str, 
                  description: str = "", date: Optional[datetime] = None) -> Optional[IncomeEntry]:
        """Add a new income entry with category validation"""
        if not self.category_manager.is_valid_category(category):
            print(f"Error: Invalid category '{category}'. Valid categories are: {self.get_available_categories()}")
            return None

        if date is None:
            date = datetime.now()
            
        entry = IncomeEntry(
            amount=amount,
            source=source,
            date=date,
            category=category.upper(),
            description=description
        )
        
        self.income_entries.append(entry)
        self._save_to_db(entry)
        return entry

    def get_available_categories(self) -> Dict[str, str]:
        """Get all available income categories"""
        return self.category_manager.get_all_categories()

    def add_custom_category(self, name: str, description: str) -> bool:
        """Add a new custom income category"""
        return self.category_manager.add_custom_category(name, description)

    def get_income_by_category(self, category: str) -> List[IncomeEntry]:
        """Filter income entries by category"""
        if not self.category_manager.is_valid_category(category):
            print(f"Warning: Invalid category '{category}'")
            return []
        return [entry for entry in self.income_entries if entry.category.upper() == category.upper()]

    def get_category_summary(self) -> Dict[str, float]:
        """Get total income by category"""
        summary = {}
        for entry in self.income_entries:
            category = entry.category.upper()
            summary[category] = summary.get(category, 0) + entry.amount
        return summary

    def get_all_income(self) -> List[IncomeEntry]:
        """Retrieve all income entries"""
        return self.income_entries

    def calculate_total_income(self) -> float:
        """Calculate total income from all entries"""
        return sum(entry.amount for entry in self.income_entries)

    def _save_to_db(self, entry: IncomeEntry) -> None:
        """Save income entry to database"""
        if self.db_connection is not None:
            # Implementation will depend on your database module
            pass