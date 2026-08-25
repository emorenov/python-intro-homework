import requests

# Warmup 1

print()
print("--- Warmup 1: Validate Numeric Input ---")

while True:
    user_input = input("Enter a number: ")
    try:
        number = float(user_input)
        break
    except ValueError:
        print("That's not a valid number. Try again.")

print(f"You entered: {number}")


# Warmup 2

print()
print("--- Warmup 2: Safe Division ---")

while True:
    numerator = float(input("Enter the numerator: "))
    denominator = float(input("Enter the denominator: "))
    try:
        result = numerator / denominator
        break
    except ZeroDivisionError:
        print("Can't divide by zero — please try a non-zero denominator.")

print(f"{numerator} ÷ {denominator} = {result}")


# Warmup 3

print()
print("--- Warmup 3: Handle a Missing File ---")

try:
    with open('../data/missing.txt', 'r') as file:
        print(file.read())
except FileNotFoundError:
    print('Error: "missing.txt" was not found. Please check the file path and try again.')


# Warmup 4

print()
print("--- Warmup 4: Virtual Environment Setup ---")

print(f"requests version: {requests.__version__}")


