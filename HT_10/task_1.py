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
from connect_db import connectdb
import random 

def change_combinations(amount, denominations,deposit):
    if deposit:
        denominations = [
            (10, 100000),
            (20, 100000),
            (50, 100000),
            (100, 100000),
            (200, 100000),
            (500, 1000000),
            (1000, 1000000)
        ]
    denominations = denominations[::-1]
    combinations = []

    for denomination, quantity in denominations:
        while amount >= denomination and quantity > 0:
            combinations.append((denomination, 1))
            amount -= denomination
            quantity -= 1

    if amount == 0:
        return combinations,None
    else:
        return None,amount


def reg_user(user_data):
    user_data = user_data.split(" ")
    if len(user_data) == 2:
        if connectdb.check_user_login(user_data):
            return "Логін вже існує"
        money = [10, 20, 50, 100, 200, 500, 1000]
        text = connectdb.register_user(user_data,random.choice(money))
        if text == "Все чудово ви зареєстровані":
            return f"User: {user_data[0]}"
        else:
            return text
    else:
        return "Неправильна вказані дані спробуйте знову!"


def login_user(user_data):
    user_data = user_data.split(" ")
    if len(user_data) == 2:
        text,user = connectdb.check_user(user_data)
        return text,user
    else:
        return "Неправильна вказані дані спробуйте знову!",None

def check_notes(notes):
    try:
        notes_list = [x for x,y in connectdb.current_notes()]
        check_list =[True if int(x) in notes_list else False for x in notes]
        if False in check_list:
            return "Вказані купюри яких не існує",None
        return "Все ок",True
    except:
        return "Введено некоректне значення",None
    


def check_amount(amount,deposit):
    try:
        if deposit:
            check_list =[True if int(x) > 0 else False for x in amount]
            if False in check_list:
                return "Вказані числа невірні",None
            return "Все ок",True
        else:
            check_list =[True if int(x) < 0 else False for x in amount]
            if False in check_list:
                return "Вказані числа невірні",None
            return "Все ок",True
    except:
        return "Введено некоректне значення",None


def taken_denominations():
    notes = (input("Введіть купюри які бажаєте забрати(номінал через пробіл): ")).split(" ")
    text,valid = check_notes(notes)
    if valid is None:
        print(text)
        return ""
    amount = (input("Введіть купюри які бажаєте забрати(кількість через пробіл): ")).split(" ")
    text_am,valid_am = check_amount(amount,False)
    if valid_am is None:
        print(text_am)
        return ""
    notes_data = list(zip(notes, amount))
    money = connectdb.update_notes(notes_data, False)
    if money == "Ok":
        return f"Ви успішно забрали {notes_data}"
    else:
        return money


def give_denominations():
    notes = (input("Введіть купюри які бажаєте додати(номінал через пробіл): ")).split(" ")
    text,valid = check_notes(notes)
    if valid is None:
        print(text)
        return ""
    amount = (input("Введіть купюри які бажаєте додати(кількість через пробіл): ")).split(" ")
    text_am,valid_am = check_amount(amount,True)
    if valid_am is None:
        print(text_am)
        return ""
    notes_data = list(zip(notes, amount))
    connectdb.update_notes(notes_data, True)
    return f"Ви успішно додали {notes_data}"


def admin_panel(user):
    admin_action = input("Оберіть дію (забрати купюри(1), положити купюри(2), переглянути купюри(3),для виходу(4) напишіть цифру дії яку бажаєте обрати: ")
    if admin_action == "1":
        taken_denominations()
        admin_panel(user)
    elif admin_action == "2":
        give_denominations()
        admin_panel(user)
    elif admin_action == "3":
        print(connectdb.current_notes())
        print(f"Загальна сума в банку {sum(denomination * quantity for denomination, quantity in connectdb.current_notes())}")
        admin_panel(user)
    elif admin_action == "4":
        print("Гарного дня!")
    else:
        print("Неправильно обрана дія!")
        admin_panel(user)


def user_panel(user):
    user_action = input("Оберіть дію (зняти кошти(1), положити кошти(2), переглянути рахунок(3),для виходу(4)) напишіть цифру дії яку бажаєте обрати: ")
    if user_action == "1":
        withdraw_cash = input("Введіть число яке хочете зняти(воно має бути додатнім): ")
        try:
            withdraw_cash = int(withdraw_cash)
            if withdraw_cash < 0:
                print("Число занадто мале!")
                user_panel(user)
            else:
                if withdraw_cash <= connectdb.current_balance(user):
                    notes,amount = change_combinations(withdraw_cash,connectdb.current_notes(),False)
                    if notes is None:
                        print(f"Нажаль таких купюри {amount} немає тому повертаємо")
                        withdraw_cash = withdraw_cash - amount
                        notes,amount = change_combinations(withdraw_cash,connectdb.current_notes(),False)
                        print(f"Ваші купюри {notes}")
                        connectdb.update_balance_withdraw(user,withdraw_cash)
                        user_panel(user)
                    else:
                        connectdb.update_balance_withdraw(user,withdraw_cash)
                        print(f"Ваші купюри {notes}")
                        user_panel(user)
                else:
                    print("У вас немає скільки коштів!")
                    user_panel(user)
        except:
            print("Неправильна дія!")
            user_panel(user)

    elif user_action == "2":
        deposit_cash = input("Введіть число яке хочете покласти на рахунок(воно має бути додатнім(обмеження для 1 поклажі: 100_000_000)): ")
        try:
            deposit_cash = int(deposit_cash)
            if deposit_cash < 0:
                print("Число занадто мале!")
                user_panel(user)
            elif deposit_cash > 100000000:
                print("Сума занадто велика!")
                user_panel(user)
            else:
                notes,amount = change_combinations(deposit_cash,connectdb.current_notes(),True)
                if notes is None:
                    print(f"Нажаль таких купюри {amount} немає тому повертаємо")
                    deposit_cash = deposit_cash - amount
                    notes,amount = change_combinations(deposit_cash,connectdb.current_notes(),True)
                    print(f"Ваші купюри {notes}")
                    connectdb.update_balance_deposit(user,deposit_cash)
                    user_panel(user)
                else:
                    print(f"Ваші купюри {notes}")
                    connectdb.update_balance_deposit(user,deposit_cash)
                    user_panel(user)
        except:
            print("Неправильна дія!")
            user_panel(user)

    elif user_action == "3":
        balance = connectdb.current_balance(user)
        print(f"Ваш баланс: {balance}")
        user_panel(user)

    elif user_action == "4":
        print("Гарного дня!")
    else:
        print("Неправильно обрана дія!")
        user_panel(user)


def start():
    start_quest = input("Для того щоб зайти в аккаунт(1), для того щоб зареєструватись (2),для виходу (3)")
    if start_quest == "1":
        login_user_quest = input("Введіть логін та пароль через відступ( )")
        login,user = login_user(login_user_quest)
        if login == "Вітаю ви зайшли до аккаунта!":
            if user == "admin":
                admin_panel(user)
            else:
                user_panel(user)
        else:
            print("Невірний логін або пароль!")
            start()
    elif start_quest == "2":
        reg_user_quest = input("Введіть логін та пароль через відступ( )")
        user = reg_user(reg_user_quest)
        if user.startswith("User: "):
            user = user.split(" ")[-1]
            user_panel(user)
        else:
            print(user)
            start()
    elif start_quest == "3":
        print("Гарного дня!")
        exit()
    else:
        print("Неправильна дія, спробуйте знову!")
        start()

def main():
    start()

if __name__ == "__main__":
    main()
