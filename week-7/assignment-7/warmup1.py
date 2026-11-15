with open('../data/notes.txt', 'r') as file:
    lines = file.readlines()  # Returns a list — one string per line

    counter = 1
    for line in lines:
        print(f"Line {counter}: {line.strip()}") # First line
        counter = counter + 1