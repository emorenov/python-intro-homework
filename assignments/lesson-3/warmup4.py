# Warmup 4: Sign (+ or -) and Parity (odd or even)
 
number = int(input("Enter a number: "))
 
# Sign check
if number > 0:
    print(f"{number} is positive.")
elif number < 0:
    print(f"{number} is negative.")
else:
    print(f"{number} is zero.")
 
# Parity check
if number % 2 == 0:
    print(f"{number} is even.")
else:
    print(f"{number} is odd.")