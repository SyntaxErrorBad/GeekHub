# 6. Написати функцію, яка буде реалізувати логіку циклічного зсуву елементів в списку. 
# Тобто функція приймає два аргументи: список і величину зсуву (якщо ця величина додатня - пересуваємо з 
# кінця на початок, якщо від'ємна - навпаки - пересуваємо елементи з початку списку в його кінець).
#    Наприклад:
#    fnc([1, 2, 3, 4, 5], shift=1) --> [5, 1, 2, 3, 4]
#    fnc([1, 2, 3, 4, 5], shift=-2) --> [3, 4, 5, 1, 2]

def check_len(length,lst):
    if length < 0:
        if length*-1 <= len(lst):
            return True
    elif length <= len(lst):
        return True
    else:
        return False


def working_with_list(lst, shift,m_shift = False):
    if m_shift:
        shift = shift%len(lst)
    if check_len(shift,lst):
        shifted_list = lst[-shift:] + lst[:-shift]
        return shifted_list
    else:
        return "Зсув занадто великий"


print(working_with_list([1, 2, 3, 4, 5], 11,m_shift=True))
