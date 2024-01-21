# 5. Написати функцію <fibonacci>, яка приймає один аргумент і виводить всі числа Фібоначчі, що не перевищують його.
def fibonacci(n):
    a, b = 0, 1
    for i in range(n):
        a, b = b, a + b
    return a


print(fibonacci(int(input("Number: "))))
