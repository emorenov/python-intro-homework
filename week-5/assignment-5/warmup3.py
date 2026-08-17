names = ["Todd", "Felipe", "Ashley", "Karen", "Sam", "Tom", "Steve", "Christina"]

guess = input("Enter a name to search for: ").strip().lower()

is_found = False
for name in names:
    if name.lower() == guess:
        is_found = True
        break

if is_found:
    print(f'"{guess}" was found in the list')
else:
    print(F'"{guess}" was not found in the list')
