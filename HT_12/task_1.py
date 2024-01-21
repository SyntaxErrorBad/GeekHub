# -*- coding: utf-8 -*-
# HT #12
# Банкомат 3.0
# - реалізуйте видачу купюр за логікою видавання найменшої кількості купюр.
# Наприклад: 2560 --> 2х1000, 1х500, 3х20. Будьте обережні з "жадібним алгоритмом"!
from connect_db import connectdb
import random
from combination_notes import find_lowest


class UserLoginReg:
    def __init__(self) -> None:
        self.user_data = None
        self.balance = None

    def check_login(self):
        return connectdb.check_user_login((self.user_data)[0])

    def check_user_valid(self):
        return connectdb.check_user(self.user_data)

    def register(self):
        user = connectdb.register_user(self.user_data, self.balance)
        if user == "Все чудово ви зареєстровані":
            return True
        else:
            return False
        
    def random_drop(self):
        money = [10, 20, 50, 100, 200, 500, 1000]
        self.balance = random.choice(money)
        if random.randint(1, 10) == 1:
            print("Вам пощастило ви виграли + 10% на баланс")
            self.balance = self.balance + (self.balance * 0.1)


class ATM_ADMIN:
    def __init__(self) -> None:
        self.user_data = "admin"
    
    def check_amount(self, amount, deposit, note=None):
        try:
            if deposit:
                check_list =[True if int(x) > 0 else False for x in amount]
                if False in check_list:
                    return "Вказані числа невірні", None
                return "Все ок", True
            else:
                notes_list = []
                note = [int(x) for x in note]
                for x, y in connectdb.current_notes():
                    for _ in note:
                        if x == _:
                            notes_list.append(y)
                check_list =[True if int(amount[x]) <= notes_list[x] else False for x in range(len(amount))]
                if False in check_list:
                    return "Вказані числа невірні", None
                return "Все ок", True
        except:
            return "Введено некоректне значення", None
    
    def check_notes(self, notes):
        try:
            notes_list = [x for x, y in connectdb.current_notes()]
            check_list =[True if int(x) in notes_list else False for x in notes]
            if False in check_list:
                return "Вказані купюри яких не існує", None
            return "Все ок", True
        except:
            return "Введено некоректне значення", None

    def taken_denominations(self):
        notes = (input("Введіть купюри які бажаєте забрати(номінал через пробіл): ")).split(" ")
        text, valid = self.check_notes(notes)
        if valid is None:
            print(text)
            return ""
        amount = (input("Введіть купюри які бажаєте забрати(кількість через пробіл): ")).split(" ")
        text_am, valid_am = self.check_amount(amount, False, notes)
        if valid_am is None:
            print(text_am)
            return ""
        notes_data = list(zip(notes, amount))
        money = connectdb.update_notes(notes_data, False)
        if money == "Ok":
            return f"Ви успішно забрали {notes_data}"
        else:
            return money

    def give_denominations(self):
        notes = (input("Введіть купюри які бажаєте додати(номінал через пробіл): ")).split(" ")
        text, valid = self.check_notes(notes)
        if valid is None:
            print(text)
            return ""
        amount = (input("Введіть купюри які бажаєте додати(кількість через пробіл): ")).split(" ")
        text_am, valid_am = self.check_amount(amount, True)
        if valid_am is None:
            print(text_am)
            return ""
        notes_data = list(zip(notes, amount))
        connectdb.update_notes(notes_data, True)
        return f"Ви успішно додали {notes_data}"


class ATM_USER:
    def __init__(self) -> None:
        self.user_data = None

    def normal_notes(self, notes):
        result = {}
        for item in notes:
            key, value = item
            if key in result:
                result[key] += value
            else:
                result[key] = value

        return '\n' + '\n'.join(list(f"{x} x {y}" for x, y in result.items()))

    def change_combinations(self, amount, denominations, deposit):
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
                return combinations, None
            else:
                return None, amount
        else:
            result, notes = find_lowest(amount, denominations)
            return result, notes
        
    def balance_user(self):
        balance = connectdb.current_balance(self.user_data)
        print(f"Ваш баланс: {balance}")

    def deposit_cash_user(self, deposit_cash):
        try:
            deposit_cash = int(deposit_cash)
            if deposit_cash < 0:
                print("Число занадто мале!")
            elif deposit_cash > 100000000:
                print("Сума занадто велика!")

            else:
                notes, amount = self.change_combinations(deposit_cash, connectdb.current_notes(), True)
                if notes is None:
                    print(f"Нажаль таких купюри {amount} немає тому повертаємо")
                    deposit_cash = deposit_cash - amount
                    notes, amount = self.change_combinations(deposit_cash, connectdb.current_notes(), True)
                    print(f"Ваші купюри: {self.normal_notes(notes)}")
                    connectdb.update_balance_deposit(self.user_data, deposit_cash)

                else:
                    print(f"Ваші купюри: {self.normal_notes(notes)}")
                    connectdb.update_balance_deposit(self.user_data, deposit_cash)
        except:
            print("Неправильна дія!")

    def withdraw_cash_user(self, withdraw_cash):
        try:
            withdraw_cash = int(withdraw_cash)
            if withdraw_cash < 0:
                print("Число за мале")
            else:
                if withdraw_cash <= connectdb.current_balance(self.user_data):
                    result, notes = self.change_combinations(withdraw_cash, connectdb.current_notes(), False)
                    if result is None:
                        bank_balance = sum(denomination * quantity for denomination, quantity in connectdb.current_notes())
                        if withdraw_cash > bank_balance:
                            print("В банкоматі недостатньо коштів для видачі!")
                        else:
                            print("В банкоматі недостатньо купюр для видачі!")

                    else:
                       connectdb.update_balance_withdraw(self.user_data, withdraw_cash)
                       connectdb.update_notes(notes, False)
                       print(f"Ваші купюри:: {result}")

                else:
                    print("У вас немає скільки коштів!")

        except:
            print("Неправильно введені дані!")


def user_panel(atm):
    user_action = input("Оберіть дію (зняти кошти(1), положити кошти(2), "
                        "переглянути рахунок(3),для виходу(4)) напишіть цифру дії яку бажаєте обрати: ")
    if user_action == "1":
        withdraw_cash = input("Введіть число яке хочете зняти(воно має бути додатнім): ")
        atm.withdraw_cash_user(withdraw_cash)
        user_panel(atm)

    elif user_action == "2":
        deposit_cash = input("Введіть число яке хочете покласти на рахунок"
                             "(воно має бути додатнім(обмеження для 1 поклажі: 100_000_000)): ")
        atm.deposit_cash_user(deposit_cash)
        user_panel(atm)

    elif user_action == "3":
        atm.balance_user()
        user_panel(atm)

    elif user_action == "4":
        print("Гарного дня")

    else:
        print("Виникла помилка")
        user_panel(atm)


def admin_panel(atm_admin):
    admin_action = input("Оберіть дію (забрати купюри(1), положити купюри(2), "
                         "переглянути купюри(3),для виходу(4) напишіть цифру дії яку бажаєте обрати: ")
    if admin_action == "1":
        atm_admin.taken_denominations()
        admin_panel(atm_admin)
    elif admin_action == "2":
        atm_admin.give_denominations()
        admin_panel(atm_admin)
    elif admin_action == "3":
        print(connectdb.current_notes())
        print(f"Загальна сума в банку "
              f"{sum(denomination * quantity for denomination, quantity in connectdb.current_notes())}")
        admin_panel(atm_admin)
    elif admin_action == "4":
        print("Гарного дня!")
    else:
        print("Неправильно обрана дія!")
        admin_panel(atm_admin)


def start():
    user = UserLoginReg()
    atm = ATM_USER()
    atm_admin = ATM_ADMIN()
    start_quest = input("Для того щоб зайти в аккаунт(1), для того щоб зареєструватись (2),для виходу (3): ")
    if start_quest == "3":
        print("Гарного дня")
        exit()

    if start_quest == "2" or start_quest == "1":
        user_data = input("Введіть логін та пароль через відступ( ): ").split(" ")
        if len(user_data) == 2:
            user.user_data = user_data
            atm.user_data = user_data
        else:
            print("Додайте пароль!")
            start()
        
    if start_quest == "1":
        user_in_db = user.check_user_valid()
        if user_in_db:
            if user_data[0] == "admin":
                admin_panel(atm_admin)
            else:
                user_panel(atm)
        else:
            print("Такого користувача не існує")
            start()
    elif start_quest == "2":
        user_in_db = user.check_login()
        if user_in_db is False:
            user.random_drop()
            if user.register():
                print(f"Вітаємо з реєстрацією {user.user_data[0]}")
                user_panel(atm)
            else:
                print("Виникла помилка спробуйте ще раз")
                start()
        else:
            print("Логін вже зайнятий")
            start()
    else:
        print("Неправильна дія, спробуйте знову!")
        start()


def main():
    start()


if __name__ == "__main__":
    main()