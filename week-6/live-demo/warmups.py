# ============================================================
# warmup1.py — Default Parameters
# ============================================================
# Write a function order(item, size="medium") that prints a
# coffee order. Call it three different ways:
#
#   1. With only an item argument
#   2. With both an item and a custom size
#   3. With the size passed as a keyword argument
#
# Expected output:
#   One medium coffee, please!
#   One large coffee, please!
#   One medium coffee, please!
# ============================================================


def order(item="Coffee", size="Medium"):
    prompt = f"One {size} {item}, please!"
    print(prompt)


order("Coffee")
order("Coffee", "Large")
order(size="Small")

print("=" * 40)
# ============================================================
# warmup2.py — Functions that Return Values
# ============================================================
# Write two functions:
#
#   miles_to_km(mi) — converts miles to km using  mi * 1.60934
#   km_to_miles(km) — converts km to miles using  km / 1.60934
#
# Call each with a few test values and print the results.
# Use f-strings and round to one decimal place.
#
# Expected output:
#   1 mi = 1.6 km
#   26.2 mi = 42.2 km
#   5 km = 3.1 mi
# ============================================================

def miles_to_km(mi):
    km = mi * 1.60934
    return km

def km_to_miles(km):
    mi = km / 1.60934
    return mi

answer = miles_to_km(1)
print(f"1 mi = {answer:.1f} km")

print(f"5 km = {km_to_miles(5):.1f} mi")
print("=" * 40)

# ============================================================
# warmup3.py — Scope in Action
# ============================================================
# Demonstrate variable scope with two short examples in one file:
#
#   1. Inside a function, calculate area = width * height for some
#      fixed width and height. Try to print(area) OUTSIDE the
#      function and show the NameError — paste the error in a
#      comment, then remove or comment out the line that causes it.
#
#   2. Show how return solves the problem: return area from the
#      function, assign it to a variable in the outer scope, and
#      print it to confirm it worked.
# ============================================================

def get_area():
    width = 10
    height = 5
    area = width * height

    return area


print(f"Area: {get_area()}")
print("=" * 40)
print()

# ============================================================
# warmup4.py — Validation Function
# ============================================================
# Write a function is_valid_rating(rating) that returns True if
# rating is an integer between 1 and 5 (inclusive), and False
# otherwise. Then use input() to ask the user for a rating.
# Call your function inside an if statement and print either:
#
#   "Valid rating."
#   "Invalid rating — must be between 1 and 5."
# ============================================================

def is_valid_rating(rating):

    if 1 <= rating <= 5:
        return True
    else:
        return False

user_rating = int(input("Enter a rating: "))

if is_valid_rating(user_rating):
    print("Valid rating.")
else:
    print("Invalid rating - must be between 1 and 5.")