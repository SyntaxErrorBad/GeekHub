# 5. Напишіть функцію,яка приймає на вхід рядок та повертає кількість окремих
# регістро-незалежних букв та цифр, які зустрічаються в рядку більше ніж 1 раз.
# Рядок буде складатися лише з цифр та букв (великих і малих). Реалізуйте обчислення
# за допомогою генератора.    Example (input string -> result):
#     "abcde" -> 0            # немає символів, що повторюються
#     "aabbcde" -> 2          # 'a' та 'b'
#     "aabBcde" -> 2          # 'a' присутнє двічі і 'b' двічі (`b` та `B`)
#     "indivisibility" -> 1   # 'i' присутнє 6 разів
#     "Indivisibilities" -> 2 # 'i' присутнє 7 разів та 's' двічі
#     "aA11" -> 2             # 'a' і '1'
#     "ABBA" -> 2             # 'A' і 'B' кожна двічі

def count_repeated_chars(s):
    s = s.lower()
    result = sum(1 for char in set(s) if s.count(char) > 1)
    return result


print(count_repeated_chars("abcde"))
print(count_repeated_chars("aabbcde"))
