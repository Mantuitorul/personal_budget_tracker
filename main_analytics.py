from datetime import datetime
from src.income import IncomeManager
from src.expenses import ExpenseManager
from src.analytics import BudgetAnalyzer, ReportGenerator

def main():
    # Create managers
    income_manager = IncomeManager()
    expense_manager = ExpenseManager()

    # Add sample income entries
    income_entries = [
        (3000.0, "Tech Corp", "SALARY", "Monthly salary"),
        (500.0, "Freelance Project", "FREELANCE", "Website development"),
        (1000.0, "Stock Dividends", "INVESTMENTS", "Q4 dividends"),
        (800.0, "Apartment 3B", "RENTAL", "December rent")
    ]

    for amount, source, category, description in income_entries:
        income_manager.add_income(
            amount=amount,
            source=source,
            category=category,
            description=description
        )

    # Add sample expense entries
    expense_entries = [
        (1500.0, "ABC Apartments", "HOUSING", "Monthly rent"),
        (400.0, "Grocery Store", "FOOD", "Monthly groceries"),
        (200.0, "Gas Station", "TRANSPORTATION", "Fuel"),
        (300.0, "Cinema & Restaurants", "ENTERTAINMENT", "Weekend activities")
    ]

    for amount, vendor, category, description in expense_entries:
        expense_manager.add_expense(
            amount=amount,
            vendor=vendor,
            category=category,
            description=description
        )

    # Create analyzer and report generator
    analyzer = BudgetAnalyzer(income_manager, expense_manager)
    report_generator = ReportGenerator(analyzer)

    # Generate and display reports
    current_date = datetime.now()
    
    print("\nMONTHLY FINANCIAL REPORT")
    print("=" * 50)
    monthly_report = report_generator.generate_monthly_report(
        current_date.year,
        current_date.month
    )
    print(monthly_report)

    print("\nTREND ANALYSIS REPORT")
    print("=" * 50)
    trend_report = report_generator.generate_trend_report(months=3)
    print(trend_report)

if __name__ == "__main__":
    main()