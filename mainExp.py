from src.expenses import ExpenseManager

def display_categories(expense_manager):
    print("\nAvailable Expense Categories:")
    for name, description in expense_manager.get_available_categories().items():
        print(f"- {name}: {description}")
    print("-" * 30)

def display_category_summary(expense_manager):
    print("\nExpense Summary by Category:")
    summary = expense_manager.get_category_summary()
    for category, total in summary.items():
        print(f"{category}: ${total:.2f}")
    print("-" * 30)

def main():
    # Create an expense manager instance
    expense_manager = ExpenseManager()

    # Display available categories
    display_categories(expense_manager)

    # Add some expense entries with different categories
    entries = [
        (1500.0, "ABC Apartments", "HOUSING", "Monthly rent"),
        (200.0, "Grocery Store", "FOOD", "Weekly groceries"),
        (60.0, "Gas Station", "TRANSPORTATION", "Car fuel"),
        (100.0, "Cinema", "ENTERTAINMENT", "Movie night"),
        (50.0, "Internet Provider", "UTILITIES", "Monthly internet")
    ]

    # Add expense entries
    for amount, vendor, category, description in entries:
        expense_manager.add_expense(
            amount=amount,
            vendor=vendor,
            category=category,
            description=description
        )

    # Add a custom category
    expense_manager.add_custom_category("PETS", "Pet care expenses")
    
    # Add expense with the new custom category
    expense_manager.add_expense(
        amount=75.0,
        vendor="Pet Store",
        category="PETS",
        description="Dog food and supplies"
    )

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

    # Display category summary
    display_category_summary(expense_manager)

    # Display total expenses
    total = expense_manager.calculate_total_expenses()
    print(f"\nTotal Expenses: ${total:.2f}")

if __name__ == "__main__":
    main()