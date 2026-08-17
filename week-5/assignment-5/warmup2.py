while True:
    entry = input("Enter a positive integer: ")

    try: 
        number = float(entry)

    except ValueError:
        print("That's not a positive integer. Try again")
        continue

    if number <= 0:
        print("That's not a positive integer. Try again")
        continue
    else:
        break

print("Got it: ", number)


        
