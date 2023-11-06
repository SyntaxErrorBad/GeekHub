# HT #07
# 1. Створіть функцію, всередині якої будуть записано список із п'яти користувачів (ім'я та пароль). 
# Функція повинна приймати три аргументи: два - обов'язкових (<username> та <password>) і 
# третій - необов'язковий параметр <silent> (значення за замовчуванням - <False>).
# Логіка наступна:
#     якщо введено коректну пару ім'я/пароль - вертається True;
#     якщо введено неправильну пару ім'я/пароль:
#         якщо silent == True - функція вертає False
#         якщо silent == False -породжується виключення LoginException (його також треба створити =))
class LoginException(Exception):
    pass


def check_username(username, password, silent=False):
    users = [
        {"username": "user1", "password": "password1"},
        {"username": "user2", "password": "password2"},
        {"username": "user3", "password": "password3"},
        {"username": "user4", "password": "password4"},
        {"username": "user5", "password": "password5"},
    ]

    for user in users:
        if user["username"] == username and user["password"] == password:
            return True
    if silent:
        return False
    else:
        raise LoginException("Invalid username or password")


try:
    username = "user1"
    password = "password1"
    if check_username(username, password):
        print("Login successful")
    else:
        print("Login failed")
except LoginException as e:
    print("LoginException:", e)
