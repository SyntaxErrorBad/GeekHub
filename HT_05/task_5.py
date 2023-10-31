# -*- coding: utf-8 -*-

# 5. Ну і традиційно - калькулятор :slightly_smiling_face: Повинна бути 1 ф-цiя,
# яка б приймала 3 аргументи - один з яких операцiя, яку зробити! Аргументи брати
# від юзера (можна по одному - 2, окремо +, окремо 2; можна всі разом - типу 1 + 2).
# Операції що мають бути присутні: +, -, *, /, %, //, **. Не забудьте протестувати з
# різними значеннями на предмет помилок!


def calculators(item):
    try:
        item = item.split()
        item = [int(i) if i.isdigit() else i for i in item]
        if item[1] == "+":
            result = item[0] + item[-1]
        elif item[1] == "-":
            result = item[0] - item[-1]
        elif item[1] == "*":
            result = item[0] * item[-1]
        elif item[1] == "/":
            if item[-1] == 0:
                return "Помилка: Ділення на нуль"
            result = item[0] / item[-1]
        elif item[1] == "%":
            result = item[0] % item[-1]
        elif item[1] == "//":
            if item[-1] == 0:
                return "Помилка: Ділення на нуль"
            result = item[0] // item[-1]
        elif item[1] == "**":
            result = item[0] ** item[-1]
        else:
            return "Помилка: Недійсна операція"

        return result

    except Exception as e:
        return f"Wrong data, Error:  {e}"


print(calculators(input("Вираз: ")))
