import os
import csv


try:
    path = os.path.join("..", "data", "example_data.csv")

    with open(path, 'r') as file:
        reader = csv.DictReader(file)
        rows = list(reader)

except FileNotFoundError:
    print("File Doesn't Exist!")

else:

    skipped_rows = []
    clean_rows = []

    for row_number, row in enumerate(rows, start=1):

        if None in row:
            key_error_message = f"Row {row_number} Skipped! KeyError - Extra Column"
            skipped_rows.append(key_error_message)
            continue

        try:
            entry = {
                "car" : row["car"],
                "model": row["model"],
                "year": int(row["year"])
            }

            clean_rows.append(entry)

        except ValueError:
            value_error_message = f"Row {row_number} - Value Error {row['year']}"
            skipped_rows.append(value_error_message)



    skipped_total = len(skipped_rows)
    clean_total = len(clean_rows)
    attempted = skipped_total + clean_total


    print("=== CSV Report ===")
    print(f"Attempted: {attempted}")
    print(f"Skipped: {skipped_total}")
    print(f"clean_total {clean_total}")

    print()
    print("Skipped Rows:")
    for row in skipped_rows:
        print(f" {row}")


    print()
    print("Clean Data:")
    for row in clean_rows:

        car = row['car']
        model = row['model']

        print(f" {car} | {model} -  {row['year']}")
        
    