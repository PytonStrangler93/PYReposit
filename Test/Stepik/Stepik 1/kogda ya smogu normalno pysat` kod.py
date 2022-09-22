# МОЁ ГОвНО
with open('dataset_3380_5.txt', 'r', encoding='utf-8') as file:
    class_list = file.read().strip().split('\n')
    first = []
    for i in class_list:
        first.append(i.split())

class_items = {i: [] for i in range(1, 12)}

for i in first:
    class_items[int(i[0])] += [int(i[2])]

with open("new_list.txt", 'w') as wr:
    for i in class_items:
        x = class_items[i]
        if len(x) != 0:
            v = sum(x) / len(x)
            class_items[i] = v
            wr.write(f'{i}' + ' ' + str(class_items[i]) + '\n')
        else:
            class_items[i] = '-'
            wr.write(f'{i}' + ' ' + str(class_items[i]) + '\n')


# СДЕЛАНО ПО ЧЕЛОвЕЧЕСКИ
# Делаем словарь {1:[0,0], 2:[0,0]... 11:[0,0]}, где [0:0] = [сумма ростов
# : кол-во учеников]
tab = {i: [0, 0] for i in range(1, 12)}

with open('dataset_3380_5.txt') as inf:

    # Заполняем словарь:
    for i in inf:
        line = i.strip().split('\t')
        tab[int(line[0])][0] += int(line[2])  # tab[класс][0] += рост ученика
        # tab[класс][1] += 1 (счетчик учеников в классе)
        tab[int(line[0])][1] += 1

    # Распечатка:
    for i in tab.keys():
        if tab[i][1] == 0:
            print(i, '-')  # распечатываем класс, в котором нет учеников
        else:
            # считаем и распечатываем средний рост для i-го класса:
            print(i, (tab[i][0] / tab[i][1]))


# import pandas as pd SHO?

#df = pd.read_table('C:\\Users\\User\\Desktop\\py_course\\dataset_3380_5.txt', header=None, sep=r'\s{1,}')
# print(df.groupby(0).mean())
