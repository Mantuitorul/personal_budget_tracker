from src.income import IncomeManager

def main():
    # Create an income manager instance
    income_manager = IncomeManager()

    # Add an income entry
    income_manager.add_income(
        amount=3000.0,
        source="Company XYZ",
        category="SALARY",
        description="Monthly salary payment"
    )

    # Display all income entries
    all_income = income_manager.get_all_income()
    for entry in all_income:
        print(f"Income Entry:")
        print(f"Amount: ${entry.amount}")
        print(f"Source: {entry.source}")
        print(f"Category: {entry.category}")
        print(f"Date: {entry.date}")
        print(f"Description: {entry.description}")
        print("-" * 30)

    # Display total income
    total = income_manager.calculate_total_income()
    print(f"\nTotal Income: ${total:.2f}")

if __name__ == "__main__":
    main()