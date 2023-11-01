# 7. Написати функцію, яка приймає на вхід список (через кому), підраховує кількість однакових елементів у 
# ньомy і виводить результат. Елементами списку можуть бути дані будь-яких типів.
#     Наприклад:
#     1, 1, 'foo', [1, 2], True, 'foo', 1, [1, 2] ----> "1 -> 3, foo -> 2, [1, 2] -> 2, True -> 1"

def count_elements(input_list):
    element_count = {}
    for element in input_list:
        if isinstance(element, (list, dict, bool)):
            element = str(element)
        if element in element_count:
            element_count[element] += 1
        else:
            element_count[element] = 1
    result = ', '.join(f"{element} -> {count}" for element, count in element_count.items())
    return result


print(count_elements([1, 1, 'foo', [1, 2], True, 'foo', 1, [1, 2]]))
