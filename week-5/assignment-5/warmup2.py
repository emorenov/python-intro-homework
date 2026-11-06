
while True:

    answer = input("Enter a positive inters: ")

    # Checks for both non-numbers and negative numbers
    # because "-5" returns false by isdigit()
    if not answer.isdigit():
        print("That's not a positive integer. Try again.")
        continue

    # convert to int
    answer = int(answer)
    
    # exit
    if answer > 0:
        print(f"Got it: {answer}")
        break