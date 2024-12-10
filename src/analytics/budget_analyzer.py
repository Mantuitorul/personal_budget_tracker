# src/analytics/budget_analyzer.py
from datetime import datetime, timedelta
from typing import Dict, List, Tuple, Optional
from ..income import IncomeManager
from ..expenses import ExpenseManager

class BudgetAnalyzer:
    def __init__(self, income_manager: IncomeManager, expense_manager: ExpenseManager):
        self.income_manager = income_manager
        self.expense_manager = expense_manager

    def get_monthly_summary(self, year: int, month: int) -> Dict[str, float]:
        """Calculate monthly summary of income, expenses, and savings"""
        total_income = self._calculate_monthly_income(year, month)
        total_expenses = self._calculate_monthly_expenses(year, month)
        savings = total_income - total_expenses
        
        return {
            'total_income': total_income,
            'total_expenses': total_expenses,
            'savings': savings,
            'savings_rate': (savings / total_income * 100) if total_income > 0 else 0
        }

    def get_category_analysis(self, year: int, month: int) -> Dict[str, Dict[str, float]]:
        """Analyze spending and income by category for a specific month"""
        income_by_category = self._get_monthly_income_by_category(year, month)
        expenses_by_category = self._get_monthly_expenses_by_category(year, month)
        
        return {
            'income': income_by_category,
            'expenses': expenses_by_category
        }

    def get_trend_analysis(self, months: int = 6) -> Dict[str, List[Dict[str, float]]]:
        """Analyze trends over the specified number of months"""
        end_date = datetime.now()
        start_date = end_date - timedelta(days=30 * months)
        
        monthly_data = []
        current_date = start_date
        
        while current_date <= end_date:
            month_summary = self.get_monthly_summary(
                current_date.year,
                current_date.month
            )
            monthly_data.append({
                'year': current_date.year,
                'month': current_date.month,
                **month_summary
            })
            # Move to next month
            if current_date.month == 12:
                current_date = datetime(current_date.year + 1, 1, 1)
            else:
                current_date = datetime(current_date.year, current_date.month + 1, 1)
        
        return {'monthly_trends': monthly_data}

    def _calculate_monthly_income(self, year: int, month: int) -> float:
        """Calculate total income for a specific month"""
        monthly_entries = [
            entry for entry in self.income_manager.get_all_income()
            if entry.date.year == year and entry.date.month == month
        ]
        return sum(entry.amount for entry in monthly_entries)

    def _calculate_monthly_expenses(self, year: int, month: int) -> float:
        """Calculate total expenses for a specific month"""
        monthly_entries = [
            entry for entry in self.expense_manager.get_all_expenses()
            if entry.date.year == year and entry.date.month == month
        ]
        return sum(entry.amount for entry in monthly_entries)

    def _get_monthly_income_by_category(self, year: int, month: int) -> Dict[str, float]:
        """Get income breakdown by category for a specific month"""
        monthly_entries = [
            entry for entry in self.income_manager.get_all_income()
            if entry.date.year == year and entry.date.month == month
        ]
        
        category_totals = {}
        for entry in monthly_entries:
            category = entry.category
            category_totals[category] = category_totals.get(category, 0) + entry.amount
        return category_totals

    def _get_monthly_expenses_by_category(self, year: int, month: int) -> Dict[str, float]:
        """Get expenses breakdown by category for a specific month"""
        monthly_entries = [
            entry for entry in self.expense_manager.get_all_expenses()
            if entry.date.year == year and entry.date.month == month
        ]
        
        category_totals = {}
        for entry in monthly_entries:
            category = entry.category
            category_totals[category] = category_totals.get(category, 0) + entry.amount
        return category_totals