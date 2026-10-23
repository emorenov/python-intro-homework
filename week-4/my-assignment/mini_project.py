list_of_students = [
    {"name": "Jazmine", "score": 88, "subject": "Python"},
    {"name": "Luis",    "score": 74, "subject": "Data"},
    {"name": "Sara",    "score": 91, "subject": "Python"},
    {"name": "Marcus",  "score": 68, "subject": "Web"},
    {"name": "Priya",   "score": 95, "subject": "Data"},
    {"name": "Devon",   "score": 72, "subject": "Python"},
    {"name": "Mia",     "score": 83, "subject": "Web"},
    {"name": "Eli",     "score": 79, "subject": "Data"},
]


# Top Scorer
highest_score = 100
highest_scoring_student = "Fake Name"

# Class average - Total Scores / Number of Scores
total = 0
# Number of Students
size_of_class = len(list_of_students)
class_average = 0

# Set of unique class subjects
unique_subjects = set()

# List of high scorers
high_scorers = []

# Top Score Bar
top_score = 90

# Looping through list of students
for student in list_of_students:
    score = student["score"]

    # Update total amount of scores
    total += score

    # Add Class Subjects to set
    subject = student["subject"]
    unique_subjects.add(subject)

    # Calculating highest scoring student
    if score > highest_score:
        highest_score = score
        highest_scoring_student = student["name"]

    if score > top_score:
        high_scorers.append(student["name"])



# After looping, calculate class average
class_average = total / size_of_class


# printing report
print(f"Top scorer: {highest_scoring_student} ({highest_score})")
print(f"Class average: {class_average}")
print(f"Subjects offered: {unique_subjects}")
print(f"High scorers: {high_scorers}")