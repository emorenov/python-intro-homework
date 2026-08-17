def order(item, size="medium"):
    print(f"One {size} {item}, please!")

# 1. Only an item (size uses its default, "medium")
order("coffee")

# 2. Item + custom size, passed positionally
order("coffee", "large")

# 3. Size passed as a keyword argument (same result as call 1)
order("coffee", size="medium")

#=================================================================

def miles_to_km(mi):
    return mi * 1.60934

def km_to_miles(km):
    return km / 1.60934

print(f"1 mi = {round(miles_to_km(1), 1)} km")
print(f"26.2 mi = {round(miles_to_km(26.2), 1)} km")
print(f"5 km = {round(km_to_miles(5), 1)} mi")


#=================================================================

# Example 1: a local variable stays trapped inside its function
def show_area():
    width = 4
    height = 3
    area = width * height

show_area()

# Trying to use `area` out here fails — it only exists inside show_area():
#
#   Traceback (most recent call last):
#     File "warmup3.py", line X, in <module>
#       print(area)
#             ^^^^
#   NameError: name 'area' is not defined
#
# print(area)   # <-- uncomment to see the NameError


# Example 2: return hands the value back out
def make_area():
    width = 4
    height = 3
    area = width * height
    return area

result = make_area()      # catch the returned value in an outer variable
print(result)             # 12



#=================================================================


def is_valid_rating(rating):
    """Return True only if rating is an int from 1 to 5 inclusive."""
    if 1 <= rating <= 5:
        return True
    else:
        return False

number = int(input("What is your rating?: "))

if is_valid_rating(number):
    print("Valid Rating")
else:
    print("Invalid Rating - must be between 1 and 5.")