# 2. Створiть 3 рiзних функцiї (на ваш вибiр). Кожна з цих функцiй повинна повертати якийсь
# результат (напр. інпут від юзера, результат математичної операції тощо). Також створiть
# четверту ф-цiю, яка всередині викликає 3 попереднi,
# обробляє їх результат та також повертає результат своєї роботи.
# Таким чином ми будемо викликати одну (четверту) функцiю, а вона в своєму тiлi - ще 3.

def function1():
    return "result func: 1"


def function2():
    return "result func: 2"


def function3():
    return "result func: 3"


def call_three_functions():
    result1 = function1()
    result2 = function2()
    result3 = function3()
    return f"result func: 1: {result1}, result func: 2: {result2}, result func: 3: {result3}"


print(call_three_functions())
