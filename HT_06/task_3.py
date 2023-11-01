# 3. Написати функцию <is_prime>, яка прийматиме 1 аргумент - число від 0 до 1000, 
# и яка вертатиме True, якщо це число просте і False - якщо ні.

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True


print(is_prime(int(input("Num: "))))
