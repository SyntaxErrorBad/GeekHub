# HT #06
# 1. Написати функцію <square>, 
# яка прийматиме один аргумент - сторону квадрата, і 
# вертатиме 3 значення у вигляді кортежа: периметр квадрата, 
# площа квадрата та його діагональ.

def square(side):
    perimeter = 4 * side
    area = side ** 2
    diagonal = (2 ** 0.5) * side
    return (perimeter, area, diagonal)


print(square(int(input("Side: "))))