# Напишите программу, которая принимает на стандартный вход список игр футбольных команд с результатом матча и
# выводит на стандартный вывод сводную таблицу результатов всех матчей.
# За победу команде начисляется 3 очка, за поражение — 0, за ничью — 1.
# Формат ввода следующий:
# В первой строке указано целое число nn — количество завершенных игр.
# После этого идет nn строк, в которых записаны результаты игры в следующем формате:
# Первая_команда;Забито_первой_командой;Вторая_команда;Забито_второй_командой
# Вывод программы необходимо оформить следующим образом:
# Команда:Всего_игр Побед Ничьих Поражений Всего_очков
# Конкретный пример ввода-вывода приведён ниже.
# Порядок вывода команд произвольный.
# Sample Input:
# 3
# Спартак;9;Зенит;10
# Локомотив;12;Зенит;3
# Спартак;8;Локомотив;15
# Sample Output:
# Спартак:2 0 0 2 0
# Зенит:2 1 0 1 3
# Локомотив:2 2 0 0 6
n = int(input())
add_counter = n
add_comm = []
while add_counter != 0:  # вкидывает пары с играми разд зяпятой списком в список
    add_comm.append(input().split(';'))
    add_counter -= 1

unique_comm_cont = []
win_list = []
lost_list = []
null_list = []
for i in add_comm:  # добавляет имена даже дублирующиесь в другой список
    unique_comm_cont.append(i[0])
    unique_comm_cont.append(i[2])
    if int(i[3]) > int(i[1]):
        win_list.append(i[2])  # победитель
        lost_list.append(i[0])  # проигравший
    elif int(i[3]) == int(i[1]):  # ничья
        null_list.append(i[2])
        null_list.append(i[0])
    else:
        win_list.append(i[0])  # победитель
        lost_list.append(i[2])  # проигравший

dict_comm = {}
for i in set(unique_comm_cont):
    dict_comm[i] = ''  # создает уникальный ключ
    dict_comm[i] = dict_comm[i] + str(unique_comm_cont.count(i))  # кол-во игр
    dict_comm[i] = dict_comm[i] + str(win_list.count(i))  # кол-во побед
    dict_comm[i] = dict_comm[i] + str(null_list.count(i))  # кол-во ничьих
    dict_comm[i] = dict_comm[i] + str(lost_list.count(i))  # кол-во поражений
    # общее знач.
    dict_comm[i] = dict_comm[i] + \
        str(null_list.count(i) + win_list.count(i) * 3)

for key in dict_comm:
    print(str(key) + ':' + ' '.join(dict_comm[key]))

# NON MINE bUT bEST
a = [input().split(';') for i in range(int(input()))]
b = {i: [] for i in set([i[0] for i in a]) | set([i[2] for i in a])}
for i in a:
    b[i[0]].append(1 if i[1] == i[3] else 3 if i[1] > i[3] else 0)
    b[i[2]].append(1 if i[1] == i[3] else 3 if i[1] < i[3] else 0)
for i in b:
    print(
        '%s:%i %i %i %i %i' %
        (i, len(
            b[i]), b[i].count(3), b[i].count(1), b[i].count(0), sum(
            b[i])))
