from src.income import IncomeManager
from src.expenses import ExpenseManager
from src.analytics import BudgetAnalyzer
from .display import (
    display_menu,
    add_income_entry,
    add_expense_entry,
    add_custom_category_entry,
    display_summaries,
    export_reports
)

def run_cli(db_manager):
    """Main CLI loop"""
    income_manager = IncomeManager(db_manager)
    expense_manager = ExpenseManager(db_manager)
    analyzer = BudgetAnalyzer(income_manager, expense_manager)

    while True:
        choice = display_menu()
        
        if choice == "0":
            print("\nThank you for using Personal Budget Tracker!")
            break
            
        actions = {
            "1": lambda: add_income_entry(income_manager),
            "2": lambda: add_expense_entry(expense_manager),
            "3": lambda: add_custom_category_entry(income_manager, "Income"),
            "4": lambda: add_custom_category_entry(expense_manager, "Expense"),
            "5": lambda: display_summaries("income", income_manager),
            "6": lambda: display_summaries("expense", expense_manager),
            "7": lambda: display_summaries("budget", income_manager, expense_manager),
            "8": lambda: export_reports(analyzer),
            "9": lambda: display_summaries("categories", income_manager, expense_manager)
        }
        
        action = actions.get(choice)
        if action:
            action()
        else:
            print("\nInvalid option. Please try again.")