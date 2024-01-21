# На основі попередньої функції (скопіюйте кусок коду) створити наступний скрипт:
#    а) створити список із парами ім'я/пароль різноманітних видів (орієнтуйтесь по правилам своєї функції) -
#    як валідні, так і ні;
#    б) створити цикл, який пройдеться по цьому циклу і, користуючись валідатором, 
#       перевірить ці дані і надрукує для кожної пари значень відповідне повідомлення, наприклад:
#       Name: vasya
#       Password: wasd
#       Status: password must have at least one digit
#       -----
#       Name: vasya
#       Password: vasyapupkin2000
#       Status: OK
#    P.S. Не забудьте використати блок try/except ;)

class ValidationException(Exception):
    pass


def check_valid(username, password):
    if len(username) < 3 or len(username) > 50:
        raise ValidationException("Username length should be between 3 and 50 characters")
    if len(password) < 8 or not any(char.isdigit() for char in password):
        raise ValidationException("Password should be at least 8 characters and contain at least one digit")
    if "geekhub" not in password:
        raise ValidationException("Password should be at geekhub!!!!!!!!")
    

users = [
        {"username": "user1", "password": "password1"},
        {"username": "user2", "password": "password2"},
        {"username": "user3", "password": "password3"},
        {"username": "user4", "password": "password4"},
        {"username": "user5", "password": "password5"},
    ]

for user in users:
    try:
        check_valid(user["username"], user["password"])
        print(f"""
            Username: {user["username"]}
            Password: {user["password"]}
            Status: OK
            --------------------
            """)

    except ValidationException as e:
        print(f"""
            Username: {user["username"]}
            Password: {user["password"]}
            Status: {e}
            --------------------
            """)
