# 6. Напишіть функцію,яка прймає рядок з декількох слів і повертає
# довжину найкоротшого слова. Реалізуйте обчислення за допомогою генератора.
def shortest_word_length(s):
    words = s.split()
    if words:
        return min(len(word) for word in words)
    return 0


print(shortest_word_length("hello hi"))
