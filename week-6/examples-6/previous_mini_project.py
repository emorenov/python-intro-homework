# mini_project_v2.py — Number Cruncher, refactored into functions

# Copied from week-5/data/numbers.py
numbers = [42, 17, 89, 3, 56, 71, 28, 94, 12, 65, 38, 7]


def find_min(numbers):
    """Return the smallest value using the accumulator pattern (no min())."""
    smallest = numbers[0]
    for number in numbers:
        if number < smallest:
            smallest = number
    return smallest


def find_max(numbers):
    """Return the largest value using the accumulator pattern (no max())."""
    largest = numbers[0]
    for number in numbers:
        if number > largest:
            largest = number
    return largest


def search(numbers, target):
    """Return the index of target, or -1 if it isn't in the list."""
    for i in range(len(numbers)):
        if numbers[i] == target:
            return i
    return -1


def bubble_sort(numbers):
    """Return a NEW sorted list. The original list is left unchanged."""
    result = numbers[:]              # make a copy first
    while True:
        swapped = False
        for i in range(len(result) - 1):
            if result[i] > result[i + 1]:
                result[i], result[i + 1] = result[i + 1], result[i]
                swapped = True
        if not swapped:
            break
    return result


def show_menu():
    """Print the menu and return the user's choice as a string."""
    print("=== Number Cruncher ===")
    print("1. Find minimum")
    print("2. Find maximum")
    print("3. Search for a number")
    print("4. Sort the list")
    print("5. Quit")
    return input("Choose an option (1-5): ")


def main():
    while True:
        choice = show_menu()
        if choice == "1":
            print(f"Minimum: {find_min(numbers)}")
        elif choice == "2":
            print(f"Maximum: {find_max(numbers)}")
        elif choice == "3":
            target = int(input("Enter a number to search for: "))
            found_at = search(numbers, target)      # search just returns the index
            if found_at != -1:                       # main() decides what to print
                print(f"Found at index {found_at}")
            else:
                print("Not found")
        elif choice == "4":
            print(f"Sorted: {bubble_sort(numbers)}")
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid option. Please choose 1-5.")
        print()  # blank line before the menu redisplays


main()