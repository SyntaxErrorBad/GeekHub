# HT_02
# 1. Write a script which accepts a sequence of comma-separated numbers from user and generate a list and a tuple with those numbers.
# 2. Write a script which accepts two sequences of comma-separated colors from user. Then print out a set containing all the colors from color_list_1 which are not present in color_list_2.
# 3. Write a script which accepts a <number> from user and print out a sum of the first <number> positive integers.
# 4. Write a script which accepts a <number> from user and then <number> times asks user for string input. At the end script must print out result of concatenating all <number> strings.
# 5. Write a script which accepts decimal number from user and converts it to hexadecimal.
# 6. Write a script to check whether a value from user input is contained in a group of values.    e.g. [1, 2, 'u', 'a', 4, True] --> 2 --> True
#          [1, 2, 'u', 'a', 4, True] --> 5 --> False
# 7. Write a script to concatenate all elements in a list into a string and print it. List must be include both strings and integers and must be hardcoded.

#1
def challenge_1():
    numbers = (input("Numbers ',': ")).split(",")
    print(numbers,tuple(numbers))

#2
def challenge_2():
    color_1,color_2 = (input("Color list 1: ")).split(","), (input("Color list 2: ")).split(",")
    print(set(color_1)-set(color_2))

#3
def challenge_3():
    number = int(input("Введіть число: "))
    sum_of_integers = sum(range(1, number + 1))
    print("Сума перших", number, "додатніх цілих чисел:", sum_of_integers)

#4
def challenge_4():
    number = int(input("Number: "))
    print("Результат конкатенації:", ''.join([str(input("Str: ")) for i in range(number)]))

#5
def challenge_5():
    print("Шістнадцяткове представлення:", hex(int(input("Введіть десяткове число: "))))

#6
def challenge_6():
    print("Чи міститься значення у списку:", input("Value: ") in ((input("Enter the value to check, separated by commas: ")).split(",")))

#7
def challenge_7():
    my_list = [1, 'два', 3, 'чотири', 5]
    print("Об'єднаний рядок:", ''.join(map(str, my_list)))

