# 4. Наприклад маємо рядок --> "f98neroi4nr0c3n30irn03ien3c0rfe  kdno400wenwkowe00koijn35pijnp46ij7k5j78p3kj546p4 65jnpoj35po6j345" -> просто потицяв по клавi =)
#    Створіть ф-цiю, яка буде отримувати рядки на зразок цього та яка оброблює наступні випадки:
# -  якщо довжина рядка в діапазонi 30-50 (включно) -> прiнтує довжину рядка, кiлькiсть букв та цифр
# -  якщо довжина менше 30 -> прiнтує суму всiх чисел та окремо рядок без цифр лише з буквами (без пробілів)
# -  якщо довжина більше 50 -> щось вигадайте самі, проявіть фантазію =)
input_string = "f98neroi4nr0c3n30irn03ien3c0rfe kdno400wenwkowe00koijn35pijnp46ij7k5j78p3kj546p4 65jnpoj35po6j345"

def process_string(input_string):
    if 30 <= len(input_string) <= 50:
        letter_count = sum(c.isalpha() for c in input_string)
        digit_count = sum(c.isdigit() for c in input_string)
        return f"Довжина рядка: {len(input_string)}, Кількість букв: {letter_count}, Кількість цифр: {digit_count}"
    elif len(input_string) < 30:
        digit_sum = sum(int(c) for c in input_string if c.isdigit())
        letters_only = ''.join(c for c in input_string if c.isalpha() and not c.isspace())
        return f"Сума всіх чисел: {digit_sum}, Рядок без цифр: {letters_only}"
    else:
        digits = [_ for _ in input_string if _.isdigit() ]
        letters = ''.join(c for c in input_string if c.isalpha() and not c.isspace())
        return " Рядок цифр :{} , Рядок букв: {}".format(''.join(digits),''.join(letters))

print(process_string(input_string))