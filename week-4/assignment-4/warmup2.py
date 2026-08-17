student = {"name": "Eduardo", "grade": 100, "subjects": ["math", "science", "english"]}

for key, value in student.items():
    print(f"{key}: {value}")

student["graduated"] = False

for key, value in student.items():
    print(f"{key}: {value}")
