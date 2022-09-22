# MAP  берет функцию которую приняла в качестве параметра и применяет ее к каждому єлементу в той последовательности которую мі тоже передали в параметре МАП
# С помощью функции мы превратим файл ТХТ который читается оболочкой как
# строка в целое число
from functools import reduce
with open('DLYA MAP.txt') as f:
    # считали первую строчку из файла и сразу превратили ее в целое число
    n = int(f.readline())
    for i in range(n):  # считываем все строчки в две переменных
        # первую укажем ту которую будем применять к итерируемой
        # последовательности
        a, b = map(int, f.readline().split())
# В качестве параметра ИНТ передается без всяких скобок мі взяли каждую
# строчку и построчно считали метод сплит разбивает по пробелу и
# возвращает строчным типом затем применяется ИНТ это преобразование в
# целое число
        print(a, b)
# Мы можем к функции МАП применять другие функции которые обьявили ранее и также их применить к какой-то итерируемой последовательности
# а также можем  взять МАП и передать ей в качестве параметров несколько
# итерируемых последовательностей.


def f(a, b):
    return a * b


# 1.1+2.1/1.2+2.2/1.3+2.3 суммирует первые-вторые-третьи строки
a = map(f, [2, 4, 5, ], [5, 6, 7])
print(list(a))  # ФУНКЦИЯ МАП ВОЗВРАЩАЕТ ОБЬЕКТ ТИПА МАП не число поэтому просто так сложить нельзя для сложения используем преобразование в список LIST
# Если списки разной длинны то перемножаются только те позиции которым есть пара, остальные не выводятся
# Еще мы можем применять МАП в лямбде


def f(a, b):
    return a * b


a = map(lambda x: x + 15, (2, 4, 5,))  # К каждому элементу добавляет 15
print(list(a))
# FILTER для фильтрации элементов последовательности


def f(a):
    if a % 2 == 0:  # задает условие четности числа
        return a


a = filter(f, (2, 4, 5,))
print(list(a))
# Через лямбду то-же самое
a = filter(lambda x: (x % 2 == 0), (2, 4, 5,))
print(list(a))
# REDUCE получает ф-цию и последовательность применяет фцию к єлem послед
# и возвращ одно значение
# РЕДУС вернет произведение всех чисел в нашей последовательности
print(reduce(lambda a, b, : a * b, (50, 57, 89, 12, 100)))
# ZIP обьединяет в кортежи несколько итерируемых последовательностей
a = [1, 2, 3, 4, 5, 6]
b = 'abcdef'
result = zip(a, b)
print(list(result))
