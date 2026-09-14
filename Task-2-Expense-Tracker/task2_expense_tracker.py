def expense_tracker():
    total = 0
    expense_count = 0

    print("===== EXPENSE TRACKER =====")

    while True:
        value = input("\nEnter an expense or type q to finish: ")

        if value.lower() == "q":
            break

        try:
            amount = float(value)

            if amount < 0:
                print("Negative expenses are not allowed.")
                continue

            total = total + amount
            expense_count = expense_count + 1

            print("Expense recorded.")
            print("Total so far:", total)

        except ValueError:
            print("Invalid amount. Please enter a number.")

    print("\n===== FINAL SUMMARY =====")
    print("Total spent:", total)
    print("Number of expenses:", expense_count)


expense_tracker()
