def display_menu():
    """Display main menu and get user choice"""
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

def display_categories(manager, type_str):
    """Display available categories"""
    print(f"\nAvailable {type_str} Categories:")
    for name, description in manager.get_available_categories().items():
        print(f"- {name}: {description}")
    print("-" * 30)

def add_income_entry(manager):
    """Handle adding new income entry"""
    print("\nAdding Income Entry")
    display_categories(manager, "Income")
    
    try:
        amount = float(input("Enter amount: $"))
        source = input("Enter source: ")
        category = input("Enter category (from above list): ").upper()
        description = input("Enter description (optional): ")
        
        entry = manager.add_income(
            amount=amount,
            source=source,
            category=category,
            description=description
        )
        
        if entry:
            print("\nIncome entry added successfully!")
        else:
            print("\nFailed to add income entry. Please check the category.")
    except ValueError:
        print("\nError: Please enter a valid number for amount.")
    except Exception as e:
        print(f"\nError adding income entry: {str(e)}")

def add_expense_entry(manager):
    """Handle adding new expense entry"""
    print("\nAdding Expense Entry")
    display_categories(manager, "Expense")
    
    try:
        amount = float(input("Enter amount: $"))
        vendor = input("Enter vendor: ")
        category = input("Enter category (from above list): ").upper()
        description = input("Enter description (optional): ")
        
        entry = manager.add_expense(
            amount=amount,
            vendor=vendor,
            category=category,
            description=description
        )
        
        if entry:
            print("\nExpense entry added successfully!")
        else:
            print("\nFailed to add expense entry. Please check the category.")
    except ValueError:
        print("\nError: Please enter a valid number for amount.")
    except Exception as e:
        print(f"\nError adding expense entry: {str(e)}")

def add_custom_category_entry(manager, type_str):
    """Handle adding new custom category"""
    print(f"\nAdding Custom {type_str} Category")
    try:
        name = input("Enter category name: ").upper()
        description = input("Enter category description: ")
        
        success = manager.add_custom_category(name, description)
        if success:
            print(f"\nCustom {type_str} category added successfully!")
        else:
            print(f"\nFailed to add custom {type_str} category. Name might already exist.")
    except Exception as e:
        print(f"\nError adding custom category: {str(e)}")

def display_summaries(summary_type, *managers):
    """Display various summaries based on type"""
    if summary_type == "income":
        print("\nIncome Summary by Category:")
        summary = managers[0].get_category_summary()
        for category, total in summary.items():
            print(f"{category}: ${total:.2f}")
    elif summary_type == "expense":
        print("\nExpense Summary by Category:")
        summary = managers[0].get_category_summary()
        for category, total in summary.items():
            print(f"{category}: ${total:.2f}")
    elif summary_type == "budget":
        income_manager, expense_manager = managers
        total_income = income_manager.calculate_total_income()
        total_expenses = expense_manager.calculate_total_expenses()
        balance = total_income - total_expenses
        
        print("\n=== BUDGET SUMMARY ===")
        print(f"Total Income: ${total_income:.2f}")
        print(f"Total Expenses: ${total_expenses:.2f}")
        print(f"Current Balance: ${balance:.2f}")
    elif summary_type == "categories":
        income_manager, expense_manager = managers
        display_categories(income_manager, "Income")
        display_categories(expense_manager, "Expense")
    print("-" * 30)

def export_reports(analyzer):
    """Handle report export"""
    try:
        year = int(input("Enter year (YYYY): "))
        month = int(input("Enter month (1-12): "))
        
        csv_path = analyzer.export_monthly_report_to_csv(year, month)
        excel_path = analyzer.export_monthly_report_to_excel(year, month)
        print(f"\nReports generated successfully:")
        print(f"CSV Report: {csv_path}")
        print(f"Excel Report: {excel_path}")
    except ValueError:
        print("\nError: Please enter valid numbers for year and month.")
    except Exception as e:
        print(f"\nError generating reports: {str(e)}")