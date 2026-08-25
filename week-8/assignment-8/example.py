import os
import csv

try:
    path = os.path.join("..", "data", "example_data.csv")

    with open(path, 'r') as file:
        reader = csv.DictReader(file)
        rows = list(reader)

except FileNotFoundError:
    print(f"ERROR: The file doesn't exist!")

else:

    skipped_rows = []
    clean_data = []

    for row_number, row in enumerate(rows, start=1):

        # check for extra columns
        if None in row:
            column_error_message = f"Row {row_number}: Extra Column!"
            skipped_rows.append(column_error_message)
            continue

        try: 
            entry = {
                "car": row["car"],
                "model": row["model"],
                "year": int(row["year"])
            }

            clean_data.append(entry)

        # check for value errors
        except ValueError:
            value_error_message = f"Row {row_number}: Value Error!"
            skipped_rows.append(value_error_message)

        # check for keyerrors
        except KeyError:
            key_error_message = f"Row {row_number}: Key Error!"
            skipped_rows.append(key_error_message)

# Summary
clean_rows = len(clean_data)
skipped = len(skipped_rows)
rows_processed = clean_rows + skipped

print("=== CSV Report ===")
print(f"Attempted: {rows_processed}")
print(f"Clean:{clean_rows}")
print(f"Skipped: {skipped}")
print()

print("Skipped Rows:")
for row in skipped_rows:
    print(f" {row}")

print()
print("Clean Data:")
for row in clean_data:
    car = row["car"]
    model = row["model"]
    year = row["year"]

    print(f" {car} | {model} | {year}")