# Выведите таблицу размером nxn, заполненную числами от 1 до n**2
# по спирали, выходящей из левого верхнего угла и закрученной по
# часовой стрелке, как показано в примере (здесь n=5n=5):
# Sample Input:
# 5
# Sample Output:
# 1 2 3 4 5
# 16 17 18 19 6
# 15 24 25 20 7
# 14 23 22 21 8
# 13 12 11 10 9
# https://www.youtube.com/watch?v=mHTMe_Q4-Xo&t=343s


n = int(input())
m = n
mas = [[0 for j in range(n)] for i in range(m)]
i = 1
x = 0
y = -1
d_row = 0  # -1 0 1
d_col = 1  # -1 0 1
length = len(str(n**2))

while i <= n**2:  # УСЛОвИЕ РАЗвОРОТА
    if 0 <= x + d_row < n and 0 <= y + \
            d_col < n and mas[x + d_row][y + d_col] == 0:
        x += d_row
        y += d_col
        mas[x][y] = i
        i += 1
    else:  # УСЛОвИЕ ДвИЖЕНИЯ ПО МАТРИЦЕ
        if d_col == 1:
            d_col = 0
            d_row = 1
        elif d_row == 1:
            d_row = 0
            d_col = -1
        elif d_col == -1:
            d_col = 0
            d_row = -1
        elif d_row == -1:
            d_row = 0
            d_col = 1

for row in mas:
    for elem in row:
        print(str(elem).rjust(length), end=" ")
    print()
