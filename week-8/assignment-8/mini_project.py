import csv
import os

try:
    path = os.path.join("..", "data", "messy_data.csv")

    with open(path, 'r') as file:
        reader = csv.DictReader(file)
        rows = list(reader)

except FileNotFoundError:
    print('Error: "messy_data.csv" was not found. Please check the file path and try again.')

else:

        clean_data = []
        skipped = []

        for row_number, row in enumerate(rows, start=1):
            if None in row:
                skipped.append(f"Row {row_number}: extra column detected — skipped")
                continue

            try:
                clean_data.append({
                    'name': row['name'],
                    'category': row['category'],
                    'amount': float(row['amount']),
                })
            except ValueError:
                skipped.append(f"Row {row_number}: ValueError — could not convert '{row['amount']}' to float")
            except KeyError as missing_key:
                skipped.append(f"Row {row_number}: KeyError — missing column {missing_key}")

        attempted = len(clean_data) + len(skipped)

        print("=== CSV Report ===")
        print(f"Rows attempted: {attempted}")
        print(f"Rows parsed: {len(clean_data)}")
        print(f"Rows skipped: {len(skipped)}")

        print("\nSkipped rows:")
        for line in skipped:
            print(f"  {line}")

        print("\nClean data:")
        for row in clean_data:
            print(f"  {row['name']} | {row['category']} | ${row['amount']:.2f}")
