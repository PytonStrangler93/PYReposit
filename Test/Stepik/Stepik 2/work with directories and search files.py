import os
import os.path


# Вам дана в архиве (ссылка) файловая структура, состоящая из директорий и файлов.
# Вам необходимо распаковать этот архив, и затем найти в данной в файловой структуре все директории, в которых есть хотя бы один файл с расширением ".py".
# Ответом на данную задачу будет являться файл со списком таких директорий, отсортированных в лексикографическом порядке.
# Для лучшего понимания формата задачи, ознакомьтесь с примером.

os.chdir('main')
b = []

for curr, dirs, files in os.walk('.'):
    for i in files:
        if i.endswith('.py'):
            b.append(curr.replace('.', 'main'))

with open("paths.txt", 'w') as x:
    for i in sorted(set(b)):
        x.write(i + '\n')
# ФАЙЛ СОХРАНЯЕТСЯ В ПАПКУ В КОТОРОЙ ИДЕТ ПОИСК
