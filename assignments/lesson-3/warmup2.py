
# Warmup 2: Age Categories
 
age = int(input("Enter your age: "))
 
if age >= 0 and age <= 12:
    category = "Child"
elif age >= 13 and age <= 17:
    category = "Teen"
elif age >= 18 and age <= 64:
    category = "Adult"
elif age >= 65:
    category = "Senior"
else:
    category = None
 
if category:
    print(f"You are a {category}.")
else:
    print("Age can't be negative.")