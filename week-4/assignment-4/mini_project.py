students = [
    {"name": "Jazmine", "score": 88, "subject": "Python"},
    {"name": "Luis",    "score": 74, "subject": "Data"},
    {"name": "Sara",    "score": 91, "subject": "Python"},
    {"name": "Marcus",  "score": 68, "subject": "Web"},
    {"name": "Priya",   "score": 95, "subject": "Data"},
    {"name": "Devon",   "score": 72, "subject": "Python"},
    {"name": "Mia",     "score": 83, "subject": "Web"},
    {"name": "Eli",     "score": 79, "subject": "Data"},
]

highest_score = 0
highest_name = ""
class_total = 0
subjects = set()
high_scorers = []

for student in students:
    score = student["score"]
    class_total += score

    if score > highest_score:
        highest_score = score
        highest_name = student["name"]

    subjects.add(student["subject"])

    if score > 75:
        high_scorers.append(student["name"])

class_average = class_total / len(students)

print(f"Top scorer:       {highest_name} ({highest_score})")
print(f"Class average:    {class_average:.1f}")
print(f"Subjects offered: {subjects}")
print(f"High scorers:     {high_scorers}")
