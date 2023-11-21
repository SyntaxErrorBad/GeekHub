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
    

def withdraw_money(user):
    withdraw_cash = int(input("Введіть суму яку бажаєте зняти(наприклад 1350(Без знака -)): "))
    if withdraw_cash < 0:
        withdraw_cash = withdraw_cash * -1

    if withdraw_cash <= connectDB.current_balance(user):
        note = change_combinations(withdraw_cash, connectDB.current_notes())
        if note is not None:
            connectDB.update_balance_withdraw(user, withdraw_cash, note)
            return f"Ви зняли {withdraw_cash} успішно"
        return f"Вибачте ви не можете зняти цю суму(Не має таких купюр)"
    return f"Замало коштів спробуйте іншу суму!"


def deposit_money(user):
    deposit_cash = int(input("Введіть суму яку бажаєте зняти(наприклад 1350(Без знака -)): "))
    note = change_combinations(deposit_cash, connectDB.current_notes())
    if note is not None:
        connectDB.update_balance_deposit(user, deposit_cash, note)
        return f"Ви положили на депозит {deposit_cash} успішно"
    return f"Вибачте ви не можете положити цю суму(Ці купюри не приймаються)"


def taken_denominations():
    notes = (input("Введіть купюри які бажаєте забрати(номінал через пробіл): ")).split(" ")
    amount = (input("Введіть купюри які бажаєте забрати(кількість через пробіл): ")).split(" ")
    notes_data = list(zip(notes, amount))
    money = connectDB.update_notes(notes_data, False)
    if money == "Ok":
        return f"Ви успішно забрали {notes_data}"
    else:
        return money


def give_denominations():
    notes = (input("Введіть купюри які бажаєте додати(номінал через пробіл): ")).split(" ")
    amount = (input("Введіть купюри які бажаєте додати(кількість через пробіл): ")).split(" ")
    notes_data = list(zip(notes, amount))
    connectDB.update_notes(notes_data, True)
    return f"Ви успішно додали {notes_data}"


def user_panel(user: str):
    if user == "admin":
        print("Для повернення в адмін панель (5)")
    user_action = input("Оберіть дію (зняти кошти(1), положити кошти(2), "
                        "переглянути рахунок(3),для виходу(4)) напишіть цифру дії яку бажаєте обрати: ")
    if user_action == "1":
        print(withdraw_money(user))
        user_panel(user)
    elif user_action == "2":
        print(deposit_money(user))
        user_panel(user)
    elif user_action == "3":
        print(connectDB.current_balance(user))
        user_panel(user)
    elif user_action == "4":
        print(f"Гарного дня {user}")
        exit()
    else:
        if user == "admin":
            if user_action == "5":
                admin_panel(user)
        print(f"Невірна команда!")
        user_panel(user)


def admin_panel(user: str):
    admin_action = input("Оберіть дію (забрати купюри(1), положити купюри(2), "
                         "переглянути купюри(3),для виходу(4),для перевірки рахунку "
                         "звичайного користувача(5)) напишіть цифру дії яку бажаєте обрати: ")
    if admin_action == "1":
        print(taken_denominations())
        admin_panel(user)
    elif admin_action == "2":
        print(give_denominations())
        admin_panel(user)
    elif admin_action == "3":
        print(connectDB.current_notes())
        admin_panel(user)
    elif admin_action == "4":
        print(f"Гарного дня {user}")
        exit()
    elif admin_action == "5":
        print(f"Ви переходите до аккаунта звичайного юзера {user}")
        user_panel(user)
    else:
        print(f"Невірна команда!")
        admin_panel(user)


def register_user():
    money = [10, 20, 50, 100, 200, 500, 1000]
    reg_quest = input("Бажаєте зареєструватись?(Так(1),Ні(2)): ")
    if reg_quest == "1":
        user = (input("Введіть логін та пароль через пробіл: ")).split(" ")
        print(connectDB.register_user(user, random.choice(money)))
        user_text, user_in_db, admin = connectDB.check_user(user)
        if user_in_db:
            print(user_text)
            if admin:
                admin_panel(user[0])
            else:
                user_panel(user[0])
        else:
            print(user_text)
            register_user()

    elif reg_quest == "2":
        user = (input("Введіть логін та пароль через пробіл: ")).split(" ")
        user_text, user_in_db, admin = connectDB.check_user(user)
        if user_in_db:
            print(user_text)
            if admin:
                admin_panel(user[0])
            else:
                user_panel(user[0])
        else:
            print(user_text)
            register_user()

    else:
        print("Неправильно обрана дія!")
        register_user()


def main():
    register_user()


if __name__ == "__main__":
    main()
