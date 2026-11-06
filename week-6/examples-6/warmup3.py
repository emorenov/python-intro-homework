# warmup3.py — Variable Scope in Action


# ─────────────────────────────────────────────
# Example 1: A variable inside a function stays inside
# ─────────────────────────────────────────────

def show_message():
    message = "I live inside the function"

show_message()

# Trying to use `message` out here fails, because it only exists
# inside show_message(). If you uncomment the line below, you get:
#
#   Traceback (most recent call last):
#     File "warmup3.py", line X, in <module>
#       print(message)
#             ^^^^^^^
#   NameError: name 'message' is not defined
#
# print(message)   # <-- uncomment to see the NameError


# ─────────────────────────────────────────────
# Example 2: return hands the value back out
# ─────────────────────────────────────────────

def make_message():
    message = "I live inside the function"
    return message          # send the value back to the caller

result = make_message()      # catch it in an outer-scope variable
print(result)                # I live inside the function