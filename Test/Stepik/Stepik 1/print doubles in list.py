# Напишите программу, которая принимает на вход список чисел в одной строке и выводит на экран в одну строку значения,
# которые встречаются в нём более одного раза.
# Для решения задачи может пригодиться метод sort списка.
# Выводимые числа не должны повторяться, порядок их вывода может быть произвольным.
# Sample Input 1:
# 4 8 0 3 4 2 0 3
# Sample Output 1:
# 0 3 4
# Sample Input 2:
# 10

my_list = [int(i) for i in input().split()]
list_2 = []
if len(my_list) <= 1:
    pass
else:
    for i in my_list:
        if my_list.count(i) > 1:
            list_2.append(i)
z = list(set(list_2))
for i in z:
    print(i, end=' ')


str = [int(i) for i in input().split()]
ans = []
[ans.append(x) for x in str if x not in ans and str.count(x) > 1]
print(*ans)
