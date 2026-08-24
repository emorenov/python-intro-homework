import os
import csv
from datetime import datetime

ACTIVITY = "Running"

path = os.path.join("..", "data", "workouts.csv")

if not os.path.exists(path):
    print("Error: workouts.csv not found.")
else:
    with open(path, 'r') as file:
        reader = csv.DictReader(file)
        workouts = list(reader)

    for row in workouts:
        row['duration_minutes'] = int(row['duration_minutes'])

    activity_workouts = [row for row in workouts if row['activity'] == ACTIVITY]
    total = sum(row['duration_minutes'] for row in activity_workouts)

    report_filename = f"{ACTIVITY.lower()}_report.txt"

    with open(report_filename, 'w') as report:
        report.write(f"{ACTIVITY} Workout Report — generated {datetime.now().strftime('%B %d, %Y')}\n")
        for row in activity_workouts:
            report.write(f"{row['date']}: {row['duration_minutes']} minutes\n")
        report.write(f"Total: {total} minutes\n")
