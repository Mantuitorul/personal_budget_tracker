from datetime import datetime, timedelta
from typing import Dict, List, Tuple, Optional
import csv
import os
from pathlib import Path
import pandas as pd
from ..income import IncomeManager
from ..expenses import ExpenseManager

class BudgetAnalyzer:
    def __init__(self, income_manager: IncomeManager, expense_manager: ExpenseManager):
        self.income_manager = income_manager
        self.expense_manager = expense_manager

        # Get the project root directory (2 levels up from this file)
        self.root_dir = Path(__file__).resolve().parent.parent.parent
        
        # Set up reports directory in project root
        self.reports_dir = self.root_dir / "reports"
        self._ensure_reports_directory()

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

    def _ensure_reports_directory(self) -> None:
        """Ensure the reports directory exists in the project root"""
        try:
            self.reports_dir.mkdir(exist_ok=True)
        except Exception as e:
            raise RuntimeError(f"Failed to create reports directory: {str(e)}")

    def export_monthly_report_to_csv(self, year: int, month: int, filename: Optional[str] = None) -> str:
        """
        Export monthly financial report to CSV
        Returns the path to the generated CSV file
        """
        # Ensure reports directory exists
        self._ensure_reports_directory()
        
        if filename is None:
            filename = f"budget_report_{year}_{month:02d}.csv"
        
        filepath = self.reports_dir / filename
        
        try:
            # Gather all data for the report
            summary = self.get_monthly_summary(year, month)
            category_analysis = self.get_category_analysis(year, month)
            
            # Prepare data for CSV
            with open(filepath, 'w', newline='') as csvfile:
                writer = csv.writer(csvfile)
                
                # Write summary section
                writer.writerow(['Monthly Summary'])
                writer.writerow(['Metric', 'Amount ($)'])
                for key, value in summary.items():
                    writer.writerow([key.replace('_', ' ').title(), f"{value:.2f}"])
                writer.writerow([])
                
                # Write income by category
                writer.writerow(['Income by Category'])
                writer.writerow(['Category', 'Amount ($)'])
                for category, amount in category_analysis['income'].items():
                    writer.writerow([category, f"{amount:.2f}"])
                writer.writerow([])
                
                # Write expenses by category
                writer.writerow(['Expenses by Category'])
                writer.writerow(['Category', 'Amount ($)'])
                for category, amount in category_analysis['expenses'].items():
                    writer.writerow([category, f"{amount:.2f}"])
            
            return str(filepath)
        except Exception as e:
            raise RuntimeError(f"Failed to export CSV report: {str(e)}")

    def export_monthly_report_to_excel(self, year: int, month: int, filename: Optional[str] = None) -> str:
        """
        Export monthly financial report to Excel
        Returns the path to the generated Excel file
        """
        # Ensure reports directory exists
        self._ensure_reports_directory()
        
        if filename is None:
            filename = f"budget_report_{year}_{month:02d}.xlsx"
        
        filepath = self.reports_dir / filename
        
        try:
            # Gather all data for the report
            summary = self.get_monthly_summary(year, month)
            category_analysis = self.get_category_analysis(year, month)
            
            # Create a Pandas Excel writer
            with pd.ExcelWriter(filepath, engine='openpyxl') as writer:
                # Monthly Summary
                summary_df = pd.DataFrame([
                    {'Metric': k.replace('_', ' ').title(), 'Amount ($)': f"{v:.2f}"}
                    for k, v in summary.items()
                ])
                summary_df.to_excel(writer, sheet_name='Monthly Summary', index=False)
                
                # Income by Category
                income_df = pd.DataFrame([
                    {'Category': k, 'Amount ($)': f"{v:.2f}"}
                    for k, v in category_analysis['income'].items()
                ])
                income_df.to_excel(writer, sheet_name='Income by Category', index=False)
                
                # Expenses by Category
                expenses_df = pd.DataFrame([
                    {'Category': k, 'Amount ($)': f"{v:.2f}"}
                    for k, v in category_analysis['expenses'].items()
                ])
                expenses_df.to_excel(writer, sheet_name='Expenses by Category', index=False)
            
            return str(filepath)
        except Exception as e:
            raise RuntimeError(f"Failed to export Excel report: {str(e)}")

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