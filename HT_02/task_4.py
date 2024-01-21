# HT_02
# 4. Write a script which accepts a <number> from user and then <number> times asks user for string input. At the end script must print out result of concatenating all <number> strings.

number = int(input("Number: "))
print("Результат конкатенації:", ''.join([str(input("Str: ")) for i in range(number)]))