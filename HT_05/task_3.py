# 3. Користувач вводить змiннi "x" та "y" з довiльними цифровими значеннями.
# Створiть просту умовну конструкцiю (звiсно вона повинна бути в тiлi ф-цiї),
# пiд час виконання якої буде перевiрятися рiвнiсть змiнних "x" та "y" та у випадку нервіності -
# виводити ще і різницю.
#     Повиннi опрацювати такi умови (x, y, z заміність на відповідні числа):
#     x > y;       вiдповiдь - "х бiльше нiж у на z"
#     x < y;       вiдповiдь - "у бiльше нiж х на z"
#     x == y.      вiдповiдь - "х дорiвнює z"

def compare_x_and_y(x, y):
    if x > y:
        return f"x більше ніж y на {x - y}"
    elif x < y:
        return f"y більше ніж x на {y - x}"
    else:
        return "x дорівнює y"


print(compare_x_and_y(2, 3))
