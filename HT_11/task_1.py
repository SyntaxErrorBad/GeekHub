# -*- coding: utf-8 -*-
# HT #11
# 1. Створити клас Calc, який буде мати атребут last_result та 4 методи. Методи повинні виконувати
# математичні операції з 2-ма числами, а саме додавання, віднімання, множення, ділення.
# - Якщо під час створення екземпляру класу звернутися до атребута last_result він повинен повернути пусте значення.
# - Якщо використати один з методів - last_result повенен повернути результат виконання ПОПЕРЕДНЬОГО методу.
#     Example:    last_result --> None
#     1 + 1
#     last_result --> None
#     2 * 3
#     last_result --> 2
#     3 * 4
#     last_result --> 6
#     ...- Додати документування в клас (можете почитати цю статтю:

class Calc:
    def __init__(self):
        self.last_r = [None, None]
        self.last_result = None

    def update_list(self, result):
        self.last_r.insert(0, result)
        self.last_r.pop()
        self.last_result = self.last_r[1]

    def add(self, x, y):
        result = x + y
        self.update_list(result)
        return result

    def subtract(self, x, y):
        result = x - y
        self.update_list(result)
        return result

    def multiply(self, x, y):
        result = x * y
        self.update_list(result)
        return result

    def divide(self, x, y):
        if y != 0:
            result = x / y
            self.update_list(result)
            return result
        else:
            print("Error: Division by zero.")
            return None


calculator = Calc()

print("last_result -->", calculator.last_result)

result_add = calculator.add(1, 1)
print("1 + 1 =", result_add)
print("last_result -->", calculator.last_result)

result_multiply = calculator.multiply(2, 3)
print("2 * 3 =", result_multiply)
print("last_result -->", calculator.last_result)

result_multiply_again = calculator.multiply(3, 4)
print("3 * 4 =", result_multiply_again)
print("last_result -->", calculator.last_result)
