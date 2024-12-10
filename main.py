from src.analytics.budget_analyzer import BudgetAnalyzer
from src.database import DatabaseManager
from src.income import IncomeManager
from src.expenses import ExpenseManager
from datetime import datetime

def display_income_categories(income_manager):
    print("\nAvailable Income Categories:")
    for name, description in income_manager.get_available_categories().items():
        print(f"- {name}: {description}")
    print("-" * 30)

def display_expense_categories(expense_manager):
    print("\nAvailable Expense Categories:")
    for name, description in expense_manager.get_available_categories().items():
        print(f"- {name}: {description}")
    print("-" * 30)

def display_income_summary(income_manager):
    print("\nIncome Summary by Category:")
    summary = income_manager.get_category_summary()
    for category, total in summary.items():
        print(f"{category}: ${total:.2f}")
    print("-" * 30)

def display_expense_summary(expense_manager):
    print("\nExpense Summary by Category:")
    summary = expense_manager.get_category_summary()
    for category, total in summary.items():
        print(f"{category}: ${total:.2f}")
    print("-" * 30)

def display_budget_summary(income_manager, expense_manager):
    total_income = income_manager.calculate_total_income()
    total_expenses = expense_manager.calculate_total_expenses()
    balance = total_income - total_expenses
    
    print("\n=== BUDGET SUMMARY ===")
    print(f"Total Income: ${total_income:.2f}")
    print(f"Total Expenses: ${total_expenses:.2f}")
    print(f"Current Balance: ${balance:.2f}")
    print("=" * 30)

def main():
    # Initialize database
    db_manager = DatabaseManager()

    # Create manager instances
    income_manager = IncomeManager(db_manager)
    expense_manager = ExpenseManager(db_manager)

    # Create budget analyzer instance
    analyzer = BudgetAnalyzer(income_manager, expense_manager)

    # Display available categories
    display_income_categories(income_manager)
    display_expense_categories(expense_manager)

    # Add some income entries
    income_entries = [
        (3000.0, "Tech Corp", "SALARY", "Monthly salary"),
        (500.0, "Freelance Project", "FREELANCE", "Website development"),
        (1000.0, "Stock Dividends", "INVESTMENTS", "Q4 dividends"),
        (800.0, "Apartment 3B", "RENTAL", "December rent")
    ]

    print("\nAdding income entries...")
    for amount, source, category, description in income_entries:
        income_manager.add_income(
            amount=amount,
            source=source,
            category=category,
            description=description
        )

    # Add custom income category and entry
    print("\nAdding custom income category...")
    income_manager.add_custom_category("YOUTUBE", "Income from YouTube channel")
    income_manager.add_income(
        amount=200.0,
        source="YouTube",
        category="YOUTUBE",
        description="Ad revenue"
    )

    # Add some expense entries
    expense_entries = [
        (1200.0, "ABC Apartments", "HOUSING", "Monthly rent"),
        (400.0, "Supermarket", "FOOD", "Groceries"),
        (150.0, "Gas Station", "TRANSPORTATION", "Monthly fuel"),
        (200.0, "Internet Provider", "UTILITIES", "Monthly internet"),
        (300.0, "Amazon", "SHOPPING", "Electronics")
    ]

    print("\nAdding expense entries...")
    for amount, vendor, category, description in expense_entries:
        expense_manager.add_expense(
            amount=amount,
            vendor=vendor,
            category=category,
            description=description
        )

    # Add custom expense category and entry
    print("\nAdding custom expense category...")
    expense_manager.add_custom_category("PETS", "Pet-related expenses")
    expense_manager.add_expense(
        amount=100.0,
        vendor="Pet Store",
        category="PETS",
        description="Dog food and supplies"
    )

    # Display all income entries
    print("\nAll Income Entries:")
    for entry in income_manager.get_all_income():
        print(f"\nIncome Entry:")
        print(f"Amount: ${entry.amount}")
        print(f"Source: {entry.source}")
        print(f"Category: {entry.category}")
        print(f"Date: {entry.date}")
        print(f"Description: {entry.description}")
    print("-" * 30)

    # Display all expense entries
    print("\nAll Expense Entries:")
    for entry in expense_manager.get_all_expenses():
        print(f"\nExpense Entry:")
        print(f"Amount: ${entry.amount}")
        print(f"Vendor: {entry.vendor}")
        print(f"Category: {entry.category}")
        print(f"Date: {entry.date}")
        print(f"Description: {entry.description}")
    print("-" * 30)

    # Display summaries
    display_income_summary(income_manager)
    display_expense_summary(expense_manager)
    display_budget_summary(income_manager, expense_manager)

    # Get current year and month for reports
    current_year = datetime.now().year
    current_month = datetime.now().month

    # Export reports using the analyzer instance
    csv_path = analyzer.export_monthly_report_to_csv(current_year, current_month)
    excel_path = analyzer.export_monthly_report_to_excel(current_year, current_month)

    print(f"\nReports generated:")
    print(f"CSV Report: {csv_path}")
    print(f"Excel Report: {excel_path}")

if __name__ == "__main__":
    main()