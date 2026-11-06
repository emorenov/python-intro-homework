# store total amount
total = 0

my_numbers = [x for x in range(101)]

for x in range(101):
    my_numbers.add(x)

# Prints 1 to 100
for x in my_numbers:
    total += x

print(total)