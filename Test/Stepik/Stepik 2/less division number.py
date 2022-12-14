# Целое положительное число называется простым, если оно имеет ровно два различных делителя, то есть делится только на единицу и на само себя.
# Например, число 2 является простым, так как делится только на 1 и 2. Также простыми являются, например, числа 3, 5, 31, и еще бесконечно много чисел.
# Число 4, например, не является простым, так как имеет три делителя – 1, 2, 4. Также простым не является число 1, так как оно имеет ровно один делитель – 1.
# Реализуйте функцию-генератор primes, которая будет генерировать простые числа в порядке возрастания, начиная с числа 2.
# Пример использования:
# print(list(itertools.takewhile(lambda x : x <= 31, primes())))
# # [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31]

def primes(n):
    mlist = [i for i in range(2, n + 1)]
    n_div = 0
    for x in mlist:
        for y in range(1, n + 1):
            if x % y == 0:
                n_div += 1
        if n_div == 2:
            print(x)
            n_div = 0
        else:
            n_div = 0


def is_prime(num):
    if num == 2:
        return True
    if num % 2 == 0:
        return False
    for _ in range(3, num // 2, 2):
        if num % _ == 0:
            return False
    return True


def primes():
    num = 2
    while True:
        if is_prime(num):
            yield num
        num += 1
