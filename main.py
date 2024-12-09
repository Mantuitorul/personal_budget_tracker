from src.income import IncomeManager

def display_categories(income_manager):
    print("\nAvailable Income Categories:")
    for name, description in income_manager.get_available_categories().items():
        print(f"- {name}: {description}")
    print("-" * 30)

def display_category_summary(income_manager):
    print("\nIncome Summary by Category:")
    summary = income_manager.get_category_summary()
    for category, total in summary.items():
        print(f"{category}: ${total:.2f}")
    print("-" * 30)

def main():
    # Create an income manager instance
    income_manager = IncomeManager()

    # Display available categories
    display_categories(income_manager)

    # Add some income entries with different categories
    entries = [
        (3000.0, "Tech Corp", "SALARY", "Monthly salary"),
        (500.0, "Freelance Project", "FREELANCE", "Website development"),
        (1000.0, "Stock Dividends", "INVESTMENTS", "Q4 dividends"),
        (800.0, "Apartment 3B", "RENTAL", "December rent")
    ]

    # Add income entries
    for amount, source, category, description in entries:
        income_manager.add_income(
            amount=amount,
            source=source,
            category=category,
            description=description
        )

    # Add a custom category
    income_manager.add_custom_category("YOUTUBE", "Income from YouTube channel")
    
    # Add income with the new custom category
    income_manager.add_income(
        amount=200.0,
        source="YouTube",
        category="YOUTUBE",
        description="Ad revenue"
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

    # Display category summary
    display_category_summary(income_manager)

    # Display total income
    total = income_manager.calculate_total_income()
    print(f"\nTotal Income: ${total:.2f}")

if __name__ == "__main__":
    main()