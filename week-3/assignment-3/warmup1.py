

# set score variable
# score 1 - 100
score = 80
grade = "D"
print(f"Score: {score}")

# 90 - 100 -> A
if score >= 90: # Greater than 90
    grade = "A"
elif score >= 80: # 80 - 89
    grade = "B"
elif score >= 70: # 70 - 79
    print(f"Grade: C")
elif score >= 60: # 60 - 69
    print(f"Grade: D")
else:               # less than 60
    print(f"Grade: F")

print(f"Grade: {grade}")