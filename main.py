from src.analytics.budget_analyzer import BudgetAnalyzer
from src.database import DatabaseManager
from src.income import IncomeManager
from src.expenses import ExpenseManager
from datetime import datetime
import argparse
import sys

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

def add_income(income_manager):
    print("\nAdding Income Entry")
    print("Available categories:")
    display_income_categories(income_manager)
    
    amount = float(input("Enter amount: $"))
    source = input("Enter source: ")
    category = input("Enter category (from above list): ").upper()
    description = input("Enter description (optional): ")
    
    entry = income_manager.add_income(
        amount=amount,
        source=source,
        category=category,
        description=description
    )
    
    if entry:
        print("\nIncome entry added successfully!")
    else:
        print("\nFailed to add income entry. Please check the category.")

def add_expense(expense_manager):
    print("\nAdding Expense Entry")
    print("Available categories:")
    display_expense_categories(expense_manager)
    
    amount = float(input("Enter amount: $"))
    vendor = input("Enter vendor: ")
    category = input("Enter category (from above list): ").upper()
    description = input("Enter description (optional): ")
    
    entry = expense_manager.add_expense(
        amount=amount,
        vendor=vendor,
        category=category,
        description=description
    )
    
    if entry:
        print("\nExpense entry added successfully!")
    else:
        print("\nFailed to add expense entry. Please check the category.")

def add_custom_category(manager, type_str):
    print(f"\nAdding Custom {type_str} Category")
    name = input("Enter category name: ").upper()
    description = input("Enter category description: ")
    
    success = manager.add_custom_category(name, description)
    if success:
        print(f"\nCustom {type_str} category added successfully!")
    else:
        print(f"\nFailed to add custom {type_str} category. Name might already exist.")

def export_reports(analyzer):
    year = int(input("Enter year (YYYY): "))
    month = int(input("Enter month (1-12): "))
    
    try:
        csv_path = analyzer.export_monthly_report_to_csv(year, month)
        excel_path = analyzer.export_monthly_report_to_excel(year, month)
        print(f"\nReports generated successfully:")
        print(f"CSV Report: {csv_path}")
        print(f"Excel Report: {excel_path}")
    except Exception as e:
        print(f"\nError generating reports: {str(e)}")

def display_menu():
    print("\n=== Personal Budget Tracker ===")
    print("1. Add Income")
    print("2. Add Expense")
    print("3. Add Custom Income Category")
    print("4. Add Custom Expense Category")
    print("5. View Income Summary")
    print("6. View Expense Summary")
    print("7. View Budget Summary")
    print("8. Export Reports")
    print("9. View Categories")
    print("0. Exit")
    return input("Select an option: ")

def interactive_mode(income_manager, expense_manager, analyzer):
    while True:
        choice = display_menu()
        
        if choice == "1":
            add_income(income_manager)
        elif choice == "2":
            add_expense(expense_manager)
        elif choice == "3":
            add_custom_category(income_manager, "Income")
        elif choice == "4":
            add_custom_category(expense_manager, "Expense")
        elif choice == "5":
            display_income_summary(income_manager)
        elif choice == "6":
            display_expense_summary(expense_manager)
        elif choice == "7":
            display_budget_summary(income_manager, expense_manager)
        elif choice == "8":
            export_reports(analyzer)
        elif choice == "9":
            display_income_categories(income_manager)
            display_expense_categories(expense_manager)
        elif choice == "0":
            print("\nThank you for using Personal Budget Tracker!")
            break
        else:
            print("\nInvalid option. Please try again.")

def main():
    parser = argparse.ArgumentParser(description='Personal Budget Tracker')
    parser.add_argument('--init-db', action='store_true', help='Initialize the database')
    args = parser.parse_args()

    # Initialize managers
    db_manager = DatabaseManager()
    income_manager = IncomeManager(db_manager)
    expense_manager = ExpenseManager(db_manager)
    analyzer = BudgetAnalyzer(income_manager, expense_manager)

    if args.init_db:
        print("Database initialized successfully!")
        return

    # Start interactive mode
    interactive_mode(income_manager, expense_manager, analyzer)

if __name__ == "__main__":
    main()