sum = 0
while True:
    n = int(input())
    if n == 0:
        break
    sum += n
print(sum)

n = int(input())  # считываем целое число
s = 0  # сумма чисел изначально равна нулю
while n != 0:  # запускаем цикл с условием
    s = s + n  # прибавляем к сумме введённое число
    n = int(input())  # просим ввести число повторно
print(s)  # выводим сумму

a = 0
while a <= 100:
    a = int(input())
    if a > 100:
        break
    if a < 10:
        continue
    print(a)

    while True:
        a = int(input())
        if a < 10:
            continue
        if a > 100:
            break
        print(a)
