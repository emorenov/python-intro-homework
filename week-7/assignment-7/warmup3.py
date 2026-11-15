import os

print(os.getcwd())

# build path
path = os.path.join("..", "data", "expenses.csv")

if os.path.exists(path):
    print("expenses.csv found.")
else:
    print("expenses.csv not found.")


print(path)
# Mac/Linux: data/sales/report.csv
# Windows:   data\sales\report.csv