#HT_03
#Write a script to get the maximum and minimum value in a dictionary.
my_dict = {'a': 10, 'b': 5, 'c': 15, 'd': [20], 'e': 5}
print("Min {}, Max {}".format(min(value for value in my_dict.values() if type(value) == int or type(value) == float ),max(value for value in my_dict.values() if type(value) == int or type(value) == float)))
