# src/expenses/expense_entry.py
from datetime import datetime
from dataclasses import dataclass

@dataclass
class ExpenseEntry:
    """Represents a single expense entry"""
    amount: float
    vendor: str
    date: datetime
    category: str
    description: str = ""
    
    def to_dict(self) -> dict:
        """Convert the expense entry to a dictionary"""
        return {
            'amount': self.amount,
            'vendor': self.vendor,
            'date': self.date.strftime('%Y-%m-%d %H:%M:%S'),
            'category': self.category,
            'description': self.description
        }
    
    @classmethod
    def from_dict(cls, data: dict) -> 'ExpenseEntry':
        """Create an ExpenseEntry instance from a dictionary"""
        return cls(
            amount=float(data['amount']),
            vendor=data['vendor'],
            date=datetime.strptime(data['date'], '%Y-%m-%d %H:%M:%S'),
            category=data['category'],
            description=data.get('description', '')
        )