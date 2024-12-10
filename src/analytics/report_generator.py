# src/analytics/report_generator.py
from datetime import datetime
from typing import Dict, List, Optional
from .budget_analyzer import BudgetAnalyzer

class ReportGenerator:
    def __init__(self, analyzer: BudgetAnalyzer):
        self.analyzer = analyzer

    def generate_monthly_report(self, year: int, month: int) -> str:
        """Generate a formatted monthly financial report"""
        summary = self.analyzer.get_monthly_summary(year, month)
        category_analysis = self.analyzer.get_category_analysis(year, month)
        
        report = f"""
Financial Report for {datetime(year, month, 1).strftime('%B %Y')}
{'-' * 50}

SUMMARY:
Total Income:    ${summary['total_income']:.2f}
Total Expenses:  ${summary['total_expenses']:.2f}
Savings:         ${summary['savings']:.2f}
Savings Rate:    {summary['savings_rate']:.1f}%

INCOME BY CATEGORY:
{'-' * 30}"""
        
        for category, amount in category_analysis['income'].items():
            report += f"\n{category:<20} ${amount:>10.2f}"
            
        report += f"\n\nEXPENSES BY CATEGORY:\n{'-' * 30}"
        
        for category, amount in category_analysis['expenses'].items():
            report += f"\n{category:<20} ${amount:>10.2f}"
            
        return report

    def generate_trend_report(self, months: int = 6) -> str:
        """Generate a trend analysis report"""
        trends = self.analyzer.get_trend_analysis(months)
        
        report = f"""
Financial Trends Report - Last {months} Months
{'-' * 50}\n"""
        
        for data in trends['monthly_trends']:
            month_date = datetime(data['year'], data['month'], 1)
            report += f"\n{month_date.strftime('%B %Y')}:"
            report += f"\n  Income:    ${data['total_income']:.2f}"
            report += f"\n  Expenses:  ${data['total_expenses']:.2f}"
            report += f"\n  Savings:   ${data['savings']:.2f}"
            report += f"\n  Rate:      {data['savings_rate']:.1f}%\n"
            
        return report