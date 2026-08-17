languages_one = ["english", "spanish", "madarin", "french"]
languages_two = ["english", "spanish", "italian", "russian", "arabic"]

languages_one_set = set(languages_one)
languages_two_set = set(languages_two)

print(f"Union: {languages_one_set.union(languages_two_set)}")
print(f"Intersection: {languages_one_set.intersection(languages_two_set)}")
print(f"Difference: {languages_one_set.difference(languages_two_set)}")

