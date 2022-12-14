# Напишите программу, на вход которой подаётся список чисел одной строкой. Программа должна для каждого
# элемента этого списка вывести сумму двух его соседей. Для элементов списка, являющихся крайними, одним из соседей
# считается элемент, находящий на противоположном конце этого списка. Например, если на вход подаётся список "1 3 5 6 10",
# то на выход ожидается список "13 6 9 15 7" (без кавычек).
# Если на вход пришло только одно число, надо вывести его же.
# Вывод должен содержать одну строку с числами нового списка, разделёнными пробелом.
# Sample Input 1:
# 1 3 5 6 10
# Sample Output 1:
# 13 6 9 15 7 type str with " "
my_list = [int(i) for i in input().split()]
if len(my_list) == 1:
    print(my_list[0])
elif len(my_list) == 2:
    print(my_list[-1] + my_list[1], my_list[0] + my_list[0], end=' ')
else:
    for i in range(len(my_list)):
        if i == len(my_list) - 1:
            print(my_list[0] + my_list[i - 1], end=' ')
        elif i == -len(my_list):
            print(my_list[i + 1] + my_list[len(my_list) - 1], end=' ')
        else:
            print(my_list[i + 1] + my_list[i - 1], end=' ')
