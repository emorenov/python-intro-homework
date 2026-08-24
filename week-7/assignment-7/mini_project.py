import os
import csv
from datetime import datetime

CATEGORY = "Transport"

path = os.path.join("..", "data", "expenses.csv")

if not os.path.exists(path):
    print("Error: expenses.csv not found.")
else:
    with open(path, 'r') as file:
        reader = csv.DictReader(file)
        expenses = list(reader)

    for row in expenses:
        row['amount'] = float(row['amount'])

    category_expenses = [row for row in expenses if row['category'] == CATEGORY]
    total = sum(row['amount'] for row in category_expenses)

    report_filename = f"{CATEGORY.lower()}_report.txt"

    with open(report_filename, 'w') as report:
        report.write(f"{CATEGORY} Expense Report — generated {datetime.now().strftime('%B %d, %Y')}\n")
        for row in category_expenses:
            report.write(f"{row['date']}: ${row['amount']}\n")
        report.write(f"Total: ${total:.2f}\n")
