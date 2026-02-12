import datetime

FILE_NAME = "expenses.txt"

def add_expense():
    amount = float(input("Enter amount: "))
    category = input("Enter category: ")
    description = input("Enter description: ")
    date = datetime.date.today()

    with open(FILE_NAME, "a") as file:
        file.write(f"{date},{amount},{category},{description}\n")

    print("✅ Expense added successfully!\n")

def view_expenses():
    try:
        with open(FILE_NAME, "r") as file:
            print("\n📄 All Expenses:")
            for line in file:
                date, amount, category, description = line.strip().split(",")
                print(f"{date} | ₹{amount} | {category} | {description}")
            print()
    except FileNotFoundError:
        print("❌ No expenses found.\n")

def total_expense():
    total = 0
    try:
        with open(FILE_NAME, "r") as file:
            for line in file:
                _, amount, _, _ = line.strip().split(",")
                total += float(amount)
        print(f"\n💰 Total Expense: ₹{total}\n")
    except FileNotFoundError:
        print("❌ No expenses found.\n")

def category_summary():
    summary = {}
    try:
        with open(FILE_NAME, "r") as file:
            for line in file:
                _, amount, category, _ = line.strip().split(",")
                summary[category] = summary.get(category, 0) + float(amount)

        print("\n📊 Category Summary:")
        for cat, amt in summary.items():
            print(f"{cat}: ₹{amt}")
        print()
    except FileNotFoundError:
        print("❌ No expenses found.\n")

def main():
    while True:
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Total Expense")
        print("4. Category Summary")
        print("5. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            total_expense()
        elif choice == "4":
            category_summary()
        elif choice == "5":
            print("👋 Exiting Expense Tracker")
            break
        else:
            print("❌ Invalid choice\n")

if __name__ == "__main__":
    main()
