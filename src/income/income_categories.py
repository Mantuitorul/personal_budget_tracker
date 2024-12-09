from enum import Enum
from typing import List, Dict

class IncomeCategory(Enum):
    SALARY = "Salary"
    FREELANCE = "Freelance"
    INVESTMENTS = "Investments"
    RENTAL = "Rental Income"
    BUSINESS = "Business Income"
    GIFTS = "Gifts"
    OTHERS = "Other Income"

class IncomeCategoryManager:
    def __init__(self):
        self._custom_categories: Dict[str, str] = {}

    def get_all_categories(self) -> Dict[str, str]:
        """Get all categories (both default and custom)"""
        categories = {category.name: category.value for category in IncomeCategory}
        categories.update(self._custom_categories)
        return categories

    def add_custom_category(self, name: str, description: str) -> bool:
        """Add a new custom category"""
        if name.upper() in [category.name for category in IncomeCategory]:
            return False
        self._custom_categories[name.upper()] = description
        return True

    def is_valid_category(self, category: str) -> bool:
        """Check if a category is valid"""
        category_upper = category.upper()
        return (category_upper in [cat.name for cat in IncomeCategory] or
                category_upper in self._custom_categories)