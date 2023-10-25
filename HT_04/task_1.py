first_start_number = True
while first_start_number:
    num1 = input("First number: ")
    try:
        num1 = int(num1)
        first_start_number = False
    except ValueError:
        try:
            num1 = float(num1)
            first_start_number = False
        except ValueError:
            print("Помилка! Введіть числове значення.")

second_start_number = True
while second_start_number:
    num2 = input("Second number: ")
    try:
        num2 = int(num2)
        second_start_number = False
    except ValueError:
        try:
            num1 = float(num2)
            second_start_number = False
        except ValueError:
            print("Помилка! Введіть числове значення.")

try:
    result = num1 / num2
    print(f"Результат ділення {num1} на {num2} дорівнює {result}")
except ZeroDivisionError:
    print("Помилка! Друге число не може бути нулем.")
except Exception as e:
    print(f"Помилка: {e}")