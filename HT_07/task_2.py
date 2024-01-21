# Створіть функцію для валідації пари ім'я/пароль за наступними правилами:
#    - ім'я повинно бути не меншим за 3 символа і не більшим за 50;
#    - пароль повинен бути не меншим за 8 символів і повинен мати хоча б одну
#    цифру;
#    - якесь власне додаткове правило :)
#    Якщо якийсь із параментів не відповідає вимогам - породити виключення із відповідним текстом.
class ValidationException(Exception):
    pass


def check_valid(username,password):

    if len(username) < 3 or len(username) > 50:
        raise ValidationException("Username length should be between 3 and 50 characters")
    if len(password) < 8 or not any(char.isdigit() for char in password):
        raise ValidationException("Password should be at least 8 characters and contain at least one digit")
    if "geekhub" not in password:
        raise ValidationException("Password should be at geekhub!!!!!!!!")
    

try:

    username = "user1"
    password = "password1geekhub"
    check_valid(username, password)
    print("Validation successful")
except ValidationException as e:
    print("ValidationException:", e)
