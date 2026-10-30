# Build a menu-driven program that loops until the user quits.
#
# === Number Cruncher ===
# 1. Find minimum
# 2. Sort the list
# 3. Quit
# Choose:
#

numbers = [8, 3, 5]
#.         0, 1, 2 

# [8, 3] -> 3, 8

# [8, 5] -> 5, 8

# 3, 5, 8

# 3, 5, 8 


while True:

    print("=== Number Cruncher ===")
    print("1. Find minimum")
    print("2. Sort the list")
    print("3. Quit")

    choice = input("Enter a choice: (1-3): ")

    if choice == "1":
        smallest = numbers[0]

        n = len(numbers) # 3
        for index in range(n): # , 3
            if numbers[index] < smallest: # 8 , 3 
                smallest = numbers[index]

        print(f'Smallest Number: {smallest} \n')

    elif choice == "2":

        """
        repeat:
            swapped = False
            for each adjacent pair:
                if left > right:
                    swap them
                    swapped = True
        until swapped is False
        """

        while True:

            swapped = False

            n = len(numbers) 
            for i in range(n - 1): 

                if numbers[i] > numbers [i + 1]:

                    numbers[i], numbers[i + 1] = numbers[i + 1], numbers[i]

                    swapped = True

            if swapped == False:
                break

        print(f'Sorted: {numbers} \n')
        

    elif choice == "3": 
        break

    else:
        print("Choose a valid numbrer \n")

