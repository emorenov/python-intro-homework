numbers = [8, 3, 5]


def find_min(numbers):
    """Return the smallest value (loop-based, no min())."""
    smallest = numbers[0]
    n = len(numbers)
    for index in range(n):
        if numbers[index] < smallest:
            smallest = numbers[index]
    return smallest


def bubble_sort(numbers):
    """Return a NEW sorted list; the original is left unchanged."""
    result = numbers.copy()              # copy first
    while True:
        swapped = False
        n = len(result)
        for i in range(n - 1):
            if result[i] > result[i + 1]:
                result[i], result[i + 1] = result[i + 1], result[i]
                swapped = True
        if swapped == False:
            break
    return result


def show_menu():
    """Print the menu and return the user's choice as a string."""
    print("=== Number Cruncher ===")
    print("1. Find minimum")
    print("2. Sort the list")
    print("3. Quit")
    return input("Enter a choice: (1-3): ")


def main():
    while True:
        choice = show_menu()
        if choice == "1":
            print(f'\nSmallest Number: {find_min(numbers)} \n')
        elif choice == "2":
            print(f'\nSorted: {bubble_sort(numbers)}\n')
        elif choice == "3":
            print("\nGoodbye!\n")
            break
        else:
            print("\nPlease enter a valid number!\n")


if __name__ == "__main__":
    main()