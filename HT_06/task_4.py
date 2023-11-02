# 4. Написати функцію <prime_list>, яка прийматиме 2 аргументи - початок і кінець діапазона, 
# і вертатиме список простих чисел всередині цього діапазона. Не забудьте про перевірку 
# на валідність введених даних та у випадку невідповідності - виведіть повідомлення.
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True


def prime_list(start, end):
    try:
        start ,end = int(start), int(end)
        primes = []
        for num in range(start, end + 1):
            if is_prime(num):
                primes.append(num)
        return primes
    except Exception as e:
        return "Неправильно введені дані, код помилки: {}".format(e)


print(prime_list(input("Start: "), input("End: ")))
