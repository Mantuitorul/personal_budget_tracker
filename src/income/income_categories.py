# income/income_categories.py
class IncomeCategories:
    """Predefined income categories"""
    
    CATEGORIES = {
        'SALARY': 'Regular employment income',
        'FREELANCE': 'Freelance or contract work',
        'INVESTMENT': 'Investment returns',
        'RENTAL': 'Rental income',
        'BUSINESS': 'Business income',
        'OTHER': 'Other income sources'
    }

    @classmethod
    def get_all_categories(cls) -> dict:
        """Get all available income categories"""
        return cls.CATEGORIES

    @classmethod
    def is_valid_category(cls, category: str) -> bool:
        """Check if a category is valid"""
        return category.upper() in cls.CATEGORIES
