# -*- coding: utf-8 -*-
# HT #10
# Банкомат 2.0
#     - усі дані зберігаються тільки в sqlite3 базі даних. Більше ніяких файлів.
#     Якщо в попередньому завданні ви добре продумали структуру програми то у вас не виникне проблем
#     швидко адаптувати її до нових вимог.
#     - на старті додати можливість залогінитися або створити новго користувача (при створенні
#     новго користувача, перевіряється відповідність логіну і паролю мінімальним вимогам.
#     Для перевірки створіть окремі функції)
#     - в таблиці (базі) з користувачами має бути створений унікальний користувач-інкасатор,
#     який матиме розширені можливості (домовимось, що логін/пароль будуть admin/admin щоб нам було простіше перевіряти)
#     - банкомат має власний баланс
#     - кількість купюр в банкоматі обмежена. Номінали купюр - 10, 20, 50, 100, 200, 500, 1000
#     - змінювати вручну кількість купюр або подивитися їх залишок в банкоматі може лише інкасатор
#     - користувач через банкомат може покласти на рахунок лише сумму кратну мінімальному
#     номіналу що підтримує банкомат. В іншому випадку - повернути "здачу"
#     (наприклад при поклажі 1005 --> повернути 5). Але це не має впливати на баланс/кількість купюр
#     банкомату, лише збільшуєтсья баланс користувача (моделюємо наявність двох незалежних касет в
#     банкоматі - одна на прийом, інша на видачу)
#     - зняти можна лише в межах власного балансу, але не більше ніж є всього в банкоматі.
#     - при неможливості виконання якоїсь операції - вивести повідомлення з причиною
#     (не вірний логін/пароль, недостатньо коштів на раунку, неможливо видати суму наявними купюрами тощо.)
import random
from connect_db import connectDB


def change_combinations(amount, denominations):
    denominations = denominations[::-1]
    combinations = []

    for denomination, quantity in denominations:
        while amount >= denomination and quantity > 0:
            combinations.append((denomination, 1))
            amount -= denomination
            quantity -= 1

    if amount == 0:
        return combinations
    else:
        return None


def control_panel(user):
    print(f"Вітаю користувача {user}")
    control_req = input("Що бажаєте зробити?(перевірити,зняти,положити): ")
    if control_req == "перевірити":
        print(f"Ваш баланс {connectDB.check_balance(user)}")
        control_panel(user)
    elif control_req == "зняти":
        withdraw_cash = int(input("Введіть суму яку хочете зняти(наприклад 1350): "))
        if withdraw_cash <= int(connectDB.check_balance(user)):
            notes_data = change_combinations(withdraw_cash, connectDB.take_notes())
            if notes_data is not None:
                print(f"Ваші купюри: {notes_data}")
                connectDB.update_balance(user, withdraw_cash, control_req, notes_data)
                print(f"Ваш баланс {connectDB.check_balance(user)}")
                control_panel(user)
            else:
                print("Нажаль не можу цього зробити, спробуйте іншу суму!")
                control_panel(user)

    elif control_req == "положити":
        withdraw_cash = int(input("Введіть суму яку хочете зняти(наприклад 1350): "))
        notes_data = change_combinations(withdraw_cash, connectDB.take_notes())
        if notes_data is not None:
            print(f"Ваші купюри: {notes_data}")
            connectDB.update_balance(user, withdraw_cash, control_req, notes_data)
            print(f"Ваш баланс {connectDB.check_balance(user)}")
            control_panel(user)
        else:
            print("Нажаль не можу цього зробити, спробуйте іншу суму!")
            control_panel(user)
    else:
        print("Неправильна дія!")
        control_panel(user)


def control_panel_admin(user):
    control_req = input("Що бажаєте зробити?(перевірити,додати,забрати): ")
    if control_req == "перевірити":
        print(f"На даний момент кількість купюр: {connectDB.take_notes()}")
        control_panel_admin(user)
    elif control_req == "додати":
        notes = (input("Введіть купюри які бажаєте додати(номінал через пробіл): ")).split(" ")
        amount = (input("Введіть купюри які бажаєте додати(кількість через пробіл): ")).split(" ")
        notes_data = list(zip(notes, amount))
        connectDB.update_notes(notes_data, control_req)
        control_panel_admin(user)

    elif control_req == "забрати":
        notes = (input("Введіть купюри які бажаєте додати(номінал через пробіл): ")).split(" ")
        amount = (input("Введіть купюри які бажаєте додати(кількість через пробіл): ")).split(" ")
        notes_data = list(zip(notes, amount))
        connectDB.update_notes(notes_data, "зняти")
        control_panel_admin(user)

    else:
        print("Неправильна дія!")
        control_panel_admin(user)


def start():
    money = [10, 20, 50, 100, 200, 500, 1000]
    register_quest = input("Бажаєте зареєструватись?(Так,Ні):")
    if register_quest == "Так":
        login, password = (input("Введіть логін та пароль(через пробіл): ")).split(" ")
        connectDB.add_user(login, password, random.choice(money))
        control_panel(login)
    elif register_quest == "Ні":
        login, password = (input("Введіть логін та пароль для перевірки(через пробіл): ")).split(" ")
        in_db, user, root = connectDB.login_valid_user(login, password)
        if in_db:
            if root:
                control_panel_admin(user)
            else:
                control_panel(user)
        else:
            print("Користувача не існує")

    else:
        print("Введено не коректне значення!")
        start()


start()
