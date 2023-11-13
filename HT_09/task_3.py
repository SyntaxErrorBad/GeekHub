# 3. Програма-банкомат.
#    Використувуючи функції створити програму з наступним функціоналом:
#       - підтримка 3-4 користувачів, які валідуються парою ім'я/пароль (файл <users.CSV>);
#       - кожен з користувачів має свій поточний баланс (файл <{username}_balance.TXT>) та
#       історію транзакцій (файл <{username_transactions.JSON>);
#       - є можливість як вносити гроші, так і знімати їх. Обов'язкова перевірка введених
#       даних (введено цифри; знімається не більше, ніж є на рахунку і т.д.).
#    Особливості реалізації:
#       - файл з балансом - оновлюється кожен раз при зміні балансу (містить просто цифру з балансом);
#       - файл - транзакціями - кожна транзакція у вигляді JSON рядка додається в кінець файла;
#       - файл з користувачами: тільки читається. Але якщо захочете реалізувати
#       функціонал додавання нового користувача - не стримуйте себе :)
#    Особливості функціонала:
#       - за кожен функціонал відповідає окрема функція;
#       - основна функція - <start()> - буде в собі містити весь workflow банкомата:
#       - на початку роботи - логін користувача (програма запитує ім'я/пароль).
#       Якщо вони неправильні - вивести повідомлення про це і закінчити роботу
#       (хочете - зробіть 3 спроби, а потім вже закінчити роботу - все на ентузіазмі :))
#       - потім - елементарне меню типн:
#         Введіть дію:
#            1. Продивитись баланс
#            2. Поповнити баланс
#            3. Вихід
#       - далі - фантазія і креатив, можете розширювати функціонал, але основне завдання
#       має бути повністю реалізоване :)
#     P.S. Увага! Файли мають бути саме вказаних форматів (csv, txt, json відповідно)
#     P.S.S. Добре продумайте структуру програми та функцій (edited) 

import csv
import json
import os
import random


def ensure_file_exists(file_path_csv):
    if not os.path.exists(file_path_csv):
        with open(file_path_csv, 'w') as file:
            pass
    
    
def ensure_file_exists_balance(file_path_txt):
    if not os.path.exists(file_path_txt):
        with open(file_path_txt, 'w') as file:
            file.write(str(random.randint(0, 20)))


def ensure_file_exists_transaction(file_path_json):
    if not os.path.exists(file_path_json):
        with open(file_path_json, 'w') as file:
            pass


def take_users(file_path_csv):
    rows = []
    with open(file_path_csv, 'r', newline='') as file:
        reader = csv.reader(file)
        for row in reader:
            rows.append(row)
    return rows


def check_valid(user_data):
    for row in take_users("users.csv"):
        if row[0] == user_data[0]:
            return True
    return False


def add_user(user_data):
    with open('users.csv', 'a+', newline='') as file:
        fieldnames = ['username', 'password']
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writerow({'username': user_data[0], 'password': user_data[-1]})


def create_files(users):
    for row in users:
        ensure_file_exists_balance("Task3_files\\balance\\"+row[0]+"_balance.txt")
        ensure_file_exists_transaction("Task3_files\\transactions\\"+row[0]+"_transactions.json")


def check_users(user_data):
    for row in take_users("users.csv"):
        if row[0] == user_data[0]:
            if row[-1] == user_data[-1]:
                return "True"
            else:
                return "Wrong Pass"
    return "No user"


def update_transactions(user_data, amount, action):
    with open("Task3_files\\transactions\\"+user_data[0]+"_transactions.json", 'r') as json_file:
        current_data = json.load(json_file)

    with open("Task3_files\\transactions\\"+user_data[0]+"_transactions.json", 'a+', encoding='utf-8') as file:
        data_to_write = {
            "Action": action,
            "Amount": amount
        }
        current_data.update(data_to_write)
        json.dump(current_data, file, indent=2)


def check_balance(user_data):
    with open("Task3_files\\balance\\"+user_data[0]+"_balance.txt", 'r') as file:
        print(f"Ваш баланс: {file.readline()}")


def update_balance(user_data, amount, action_name):
    with open("Task3_files\\balance\\"+user_data[0]+"_balance.txt", 'r') as file:
        past_amount = file.readline()

    with open("Task3_files\\balance\\"+user_data[0]+"_balance.txt", 'w') as file:
        if action_name == "поповнити":
            file.write(str(int(past_amount)+int(amount)))
        elif action_name == "зняти кошти":
            if int(past_amount) > int(amount):
                file.write(str(int(past_amount)-int(amount)))
            else:
                print("Сума зняття завелика!")
                control(user_data)

    update_transactions(user_data, action=action_name, amount=amount)
    control(user_data)
    

def control(user_data):
    abillity = input("Введіть що бажаєте(переглянути баланс,поповнити,зняти кошти,вихід): ")
    if abillity == "переглянути баланс":
        check_balance(user_data)
    elif abillity == "поповнити":
        amount = input("Сума поповнення?: ")
        update_balance(user_data, amount, abillity)
    elif abillity == "зняти кошти":
        amount = input("Сума зняття: ")
        update_balance(user_data, amount, abillity)
    elif abillity == "вихід":
        exit()


def login(password=1):
    login_in = (input("Введіть ім'я та пароль через пробіл: ")).split(" ")
    user = check_users(login_in)
    if user == "True":
        print(f"Вітаю ви зайшли під ім'ям: {login_in[0]}")
        control(login_in)
    elif user == "Wrong Pass":
        if password != 3:
            print("Ви ввели невірний пароль залогіньтесь знову")
            login(password + 1)
        else:
            print("Ви витратили всі спроби! Допобаченя!")
            exit()
    elif user == "No user":
        print("Нажаль такого користувача не існує")
        start()


def start():
    reg_quest = input("Бажаєте зареєструватись?: ")
    if reg_quest == "Yes":
        user_data = (input("Через пробіл напишіть ім'я та пароль: ")).split(" ")
        if check_valid(user_data):
            print("Нажаль користувач існує")
            start()
        else:
            add_user(user_data=user_data)
            create_files(take_users("users.csv"))
            print(f"Вітаю ви зайшли під ім'ям: {user_data[0]}")
            control(user_data)
    elif reg_quest == "No":
        print("Зайдіть до свого аккаунта!")
        login()


def main():
    ensure_file_exists("users.csv")
    create_files(take_users("users.csv"))
    start()
    print(take_users("users.csv"))


if __name__ == "__main__":
    main()
