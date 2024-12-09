from enum import Enum
from typing import Dict

class ExpenseCategory(Enum):
    HOUSING = "Housing expenses (rent, mortgage, utilities)"
    FOOD = "Food and groceries"
    TRANSPORTATION = "Transportation (fuel, public transit, maintenance)"
    HEALTHCARE = "Healthcare and medical expenses"
    ENTERTAINMENT = "Entertainment and recreation"
    SHOPPING = "Shopping (clothing, electronics)"
    EDUCATION = "Education and training"
    UTILITIES = "Utilities (electricity, water, internet)"
    INSURANCE = "Insurance premiums"
    DEBT = "Debt payments"
    SAVINGS = "Savings and investments"
    OTHERS = "Other expenses"

class ExpenseCategoryManager:
    def __init__(self):
        self._custom_categories: Dict[str, str] = {}

    def get_all_categories(self) -> Dict[str, str]:
        """Get all categories (both default and custom)"""
        categories = {category.name: category.value for category in ExpenseCategory}
        categories.update(self._custom_categories)
        return categories

    def add_custom_category(self, name: str, description: str) -> bool:
        """Add a new custom category"""
        if name.upper() in [category.name for category in ExpenseCategory]:
            return False
        self._custom_categories[name.upper()] = description
        return True

    def is_valid_category(self, category: str) -> bool:
        """Check if a category is valid"""
        category_upper = category.upper()
        return (category_upper in [cat.name for cat in ExpenseCategory] or
                category_upper in self._custom_categories)
