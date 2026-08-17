numbers = [1, 2, 3, 4, 5, 6, 7, 8]

print(f"First: {numbers[0]}")
print(f"Last: {numbers[-1]}")
print(f"Middle: {numbers[2:6]}")

reversed_numbers = []

for index in range(7,-1,-1):
    reversed_numbers.append(numbers[index])

print(f"Reversed: {reversed_numbers}")