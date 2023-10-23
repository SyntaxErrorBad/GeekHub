#HT_03
# Write a script to remove values duplicates from dictionary. Feel free to hardcode your dictionary.
my_dict = {'a': 1, 'b': 2, 'c': 1, 'd': 3, 'e': 2, 'f': 4}
unique_dict = {}
for key, value in my_dict.items():
    if value not in unique_dict.values():
        unique_dict[key] = value

print(unique_dict)