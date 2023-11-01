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
        primes = []
        for num in range(start, end + 1):
            if is_prime(num):
                primes.append(num)
        return primes
    except Exception as e:
        return e


print(prime_list(int(input("Start: ")), int(input("End: "))))
