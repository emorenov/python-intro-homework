# Copied from week-5/data/numbers.py
numbers = [42, 17, 89, 3, 56, 71, 28, 94, 12, 65, 38, 7]

while True:
    print("=== Number Cruncher ===")
    print("1. Find minimum")
    print("2. Find maximum")
    print("3. Search for a number")
    print("4. Sort the list")
    print("5. Quit")
    choice = input("Choose an option (1-5): ")

    if choice == "1":
        # Track the smallest value (accumulator pattern)
        smallest = numbers[0]
        for number in numbers:
            if number < smallest:
                smallest = number
        print(f"Minimum: {smallest}")

    elif choice == "2":
        # Track the largest value
        largest = numbers[0]
        for number in numbers:
            if number > largest:
                largest = number
        print(f"Maximum: {largest}")

    elif choice == "3":
        target = int(input("Enter a number to search for: "))
        found_at = -1
        for i in range(len(numbers)):
            if numbers[i] == target:
                found_at = i
                break
        if found_at != -1:
            print(f"Found {target} at index {found_at}")
        else:
            print(f"{target} is not in the list.")

    elif choice == "4":
        # Bubble sort — repeat passes until one pass makes no swaps
        while True:
            swapped = False
            for i in range(len(numbers) - 1):
                if numbers[i] > numbers[i + 1]:
                    numbers[i], numbers[i + 1] = numbers[i + 1], numbers[i]
                    swapped = True
            if not swapped:
                break
        print(f"Sorted: {numbers}")

    elif choice == "5":
        print("Goodbye!")
        break

    else:
        print("Invalid option. Please choose 1-5.")

    print()  # blank line before the menu redisplays