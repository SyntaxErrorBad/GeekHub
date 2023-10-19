# HT_02
# 3. Write a script which accepts a <number> from user and print out a sum of the first <number> positive integers.

number = int(input("Введіть число: "))
sum_of_integers = sum(range(1, number + 1))
print("Сума перших", number, "додатніх цілих чисел:", sum_of_integers)