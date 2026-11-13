# Demo: Workout Report Generator
#
# The file ../data/workouts.csv tracks workout sessions:
# date,activity,duration_minutes
# 2024-03-01,Running,30
# 2024-03-02,Yoga,45
# ...
#
# Write a program that:
# 1. Uses os.path.exists() to verify ../data/workouts.csv exists before
#    opening it. Print an error and stop if it doesn't.
# 2. Reads the file into a list of dictionaries using csv.DictReader.
# 3. Converts duration_minutes to int for each row.
# 4. Filters the list to only rows where activity is "Running".
# 5. Calculates the total minutes spent running.
# 6. Writes a report to running_report.txt:
#    - First line: Running Workout Report — generated [today's date]
#    - One line per session: [date]: [duration_minutes] minutes
#    - Last line: Total: [total] minutes

import os
import csv
import datetime

ACTIVITY = "Yoga"

path = os.path.join("..", "data", "workouts.csv")

if not os.path.exists(path):
    print("File Doesn't Exist!")
else:
    with open(path, 'r') as file:
        reader = csv.DictReader(file)
        workouts = list(reader)

    for row in workouts:
        row['duration_minutes'] = int(row['duration_minutes'])

    activity_workout = [row for row in workouts if row['activity'] == ACTIVITY]


    total = sum(row['duration_minutes'] for row in activity_workout)


    report_name = f"{ACTIVITY}_report.txt"

    with open(report_name, 'w') as report:
        report.write(f"{ACTIVITY} Report - generated {datetime.datetime.now().strftime('%B %d, %Y')} \n")

        for row in activity_workout:
            report.write(f" {row['date']}: {row['duration_minutes']} minutes \n")

        report.write(f"Total: {total} minutes \n")



"""
example data  
[
{ "date": "08-12-2026", "activity": "Running", "duration_minutes": "30"},
{ "date": "08-12-2026", "activity": "Yoga", "duration_minutes": "30"},
{ "date": "08-12-2026", "activity": "Cycling", "duration_minutes": "30"},
]
"""
