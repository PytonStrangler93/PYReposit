a , b = int(input()), int(input())
total_maximum = 0                    # сумма делителей
digit = 0                            # число с максимальной суммой делителей

for i in range(a, b + 1):             # цикл перебирающий все числа от a до b включительно
    maximum = 0                       # обнуление суммы делителей, для нового цикла
    for j in range(1, i + 1):         # проверяем все числа от 1 до числа не превышающего проверяемое
        if i % j == 0:                # проверка на деление без остатка
            maximum += j              # суммируем делители
        if maximum >= total_maximum:  # если сумма делителей больше max суммы делителей
            total_maximum = maximum   # записываем в переменную максимальную
            digit = j
print(digit, total_maximum)




# n Обратите внимание на второй аргумент функции sum, задающий начальное значение суммы делителей. В случае когда число является точным квадратом - сумму делителей заранее уменьшается на величину \sqrt{n} 
# n, что связано с тем что на каждой итерации к сумме добавляются сразу 2 делителя i и n//i, а для точного квадрата его корень будет подсчитан дважды в качестве делителя! 
# Так же обратите внимание на нестрогое неравенство dsum >=msum. Это необходимо для выполнения условия: Если таких чисел несколько, то выведите наибольшее из них.
# Сравнивать сами числа в случае равенства нет необходимости, потому что текущее число всегда больше предидущих.


a, b, mnum, msum = int(input()), int(input()), 0, 0
for num in range(a, b+1):
    sqrt = int(num**0.5)
    dsum = sum((i+num//i for i in range(1, sqrt+1) if num%i == 0), -sqrt if sqrt**2==num else 0)
    if dsum >= msum:
        mnum, msum = num, dsum
print(mnum, msum)

#!!!!!!!!!!!!!!!
a, b = int(input()), int(input())
x = [sum([j for j in range(1,i+1) if i%j == 0]) for i in range(a,b+1)]
print(x.index(max(x))+a, max(x) )




print(*max([[i] + [sum([e for e in range(1, i + 1) if not i % e])] for i in range(int(input()), int(input()) + 1)], key=lambda x: (x[1], x[0])))