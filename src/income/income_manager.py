from datetime import datetime
from typing import List, Optional
from .income_entry import IncomeEntry

class IncomeManager:
    """Manages income entries and operations"""
    
    def __init__(self, db_connection=None):
        self.income_entries: List[IncomeEntry] = []
        self.db_connection = db_connection

    def add_income(self, amount: float, source: str, category: str, 
                  description: str = "", date: Optional[datetime] = None) -> IncomeEntry:
        """Add a new income entry"""
        if date is None:
            date = datetime.now()
            
        entry = IncomeEntry(
            amount=amount,
            source=source,
            date=date,
            category=category,
            description=description
        )
        
        self.income_entries.append(entry)
        self._save_to_db(entry)
        return entry

    def get_all_income(self) -> List[IncomeEntry]:
        """Retrieve all income entries"""
        return self.income_entries

    def get_income_by_category(self, category: str) -> List[IncomeEntry]:
        """Filter income entries by category"""
        return [entry for entry in self.income_entries if entry.category.lower() == category.lower()]

    def calculate_total_income(self) -> float:
        """Calculate total income from all entries"""
        return sum(entry.amount for entry in self.income_entries)

    def _save_to_db(self, entry: IncomeEntry) -> None:
        """Save income entry to database"""
        if self.db_connection is not None:
            # Implementation will depend on your database module
            pass