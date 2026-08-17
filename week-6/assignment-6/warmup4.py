def is_valid_score(score):
    """Return True only if score is an int from 0 to 100 inclusive."""
    if 0 <= score <= 100:
        return True
    else:
        return False

number = int(input("What is your score?: "))

if is_valid_score(number):
    print("Valid Score")
else:
    print("Invalid Score - must be between 0 and 100.")
