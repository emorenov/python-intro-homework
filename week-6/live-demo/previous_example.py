# Build a menu-driven program that loops until the user quits.
#
# === Number Cruncher ===
# 1. Find minimum
# 2. Sort the list
# 3. Quit
# Choose:
#

def menu():
    """Shows the menu options"""
    print("=== Number Cruncher ===")
    print("1. Find minimum")
    print("2. Sort the list")
    print("3. Quit")

    answer = input("Enter a choice: (1-3): ")

    return answer

def find_minimum(nums):
        """Return the smallest value. """
        smallest = nums[0]

        n = len(nums)
        for index in range(n):
            if nums[index] < smallest:
                smallest = nums[index]

        return smallest

def sort_nums(unsorted_numbers):

        unsorted_nums = unsorted_numbers.copy() # unsorted_numbers[:]

        while True:

            swapped = False

            n = len(unsorted_nums) 
            for i in range(n - 1): 

                if unsorted_nums[i] > unsorted_nums [i + 1]:

                    unsorted_nums[i], unsorted_nums[i + 1] = unsorted_nums[i + 1], unsorted_nums[i]

                    swapped = True

            if swapped == False:
                break

        return unsorted_nums




def main():

    numbers = [8, 3, 5, 1]


    while True:

        choice = menu()

        if choice == "1":

            print(f'\nSmallest Number: {find_minimum(numbers)} \n')

        elif choice == "2":

            print(f'\nSorted: {sort_nums(numbers)}\n')
            print(f"\nOriginal List: {numbers}\n")
            

        elif choice == "3": 

            print("\nGoodbye!\n")
            break

        else:
            print("\nPlease enter a valid number!\n")


if __name__ == "__main__":
     main()