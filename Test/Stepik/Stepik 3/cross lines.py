# На числовой прямой даны два отрезка: Напишите программу, которая находит их пересечение.
# Пересечением двух отрезков может быть:
# отрезок;
# точка;
# пустое множество.
# Формат входных данных
# На вход программе подаются 4 целых числа каждое на отдельной строке. 
# Формат выходных данных
# Программа должна вывести на экран границы отрезка, являющегося пересечением, либо общую точку, либо текст «пустое множество».
# Sample Input 1:
# 1
# 3
# 2
# 4
# Sample Output 1:
# 2 3
# Sample Input 2:
# 1
# 2
# 3
# 4
# Sample Output 2:
# пустое множество
# Sample Input 3:
# 5
# 6
# 6
# 8
# Sample Output 3:
# 6



start1, end1, start2, end2 = (int(input()) for a in range(4))
first = range(start1, end1 + 1)
second = range(start2, end2 + 1)
general = [a for a in first if a in second]
if len(general) == 0:
    print('пустое множество ')
else:
    print(*sorted({general[0], general[-1]}))
