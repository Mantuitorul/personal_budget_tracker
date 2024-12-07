from datetime import datetime
from dataclasses import dataclass

@dataclass
class IncomeEntry:
    """Represents a single income entry"""
    amount: float
    source: str
    date: datetime
    category: str
    description: str = ""
    
    def to_dict(self) -> dict:
        """Convert the income entry to a dictionary"""
        return {
            'amount': self.amount,
            'source': self.source,
            'date': self.date.strftime('%Y-%m-%d %H:%M:%S'),
            'category': self.category,
            'description': self.description
        }
    
    @classmethod
    def from_dict(cls, data: dict) -> 'IncomeEntry':
        """Create an IncomeEntry instance from a dictionary"""
        return cls(
            amount=float(data['amount']),
            source=data['source'],
            date=datetime.strptime(data['date'], '%Y-%m-%d %H:%M:%S'),
            category=data['category'],
            description=data.get('description', '')
        )