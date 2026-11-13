with open('../data/notes.txt', 'r') as file:
    line_number = 1
    for line in file:
        print(f"Line {line_number}: {line.strip()}")
        line_number += 1


    # for number, line in enumerate(file, start=1):
    #     print(f"Line {number}: {line.strip()}")