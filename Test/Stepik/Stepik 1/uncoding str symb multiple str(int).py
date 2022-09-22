with open('dataset_3363_2.txt', 'r') as f:
    n = f.readline().strip()  # Чтение из файла

x = n
letters = """abcdefghijklmnopqrstuvwxyz!"#$%&'()*+,-./"""  # Набор символов для сравнения
let = ''
all_let = []  # входная строка в список
for i in x:  # выборка букв в строку из общей строки
    if i.lower() in letters:
        let += i

for i in x:  # преобразование всей входной строки в элементы списка
    all_let += i
iterator = 0
while iterator <= len(
        all_let) - 1:  # если элемент списка можно превратить в число пропуск если нет замена его на запятую
    for i in all_let:
        try:
            int(all_let[iterator])
        except BaseException:
            ValueError
            all_let[iterator] = ','
    iterator += 1
# удаление ненужных символов и перевод в список
v = ''.join(all_let).strip(',').split(',')

iterator2 = 0
into_file = ''
while iterator2 <= len(let) - 1:  # делает готовую итоговую строку
    into_file += let[iterator2] * int(v[iterator2])
    iterator2 += 1


with open("HM.txt", 'w') as w:
    w.write(into_file)
    w.close
