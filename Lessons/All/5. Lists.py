LIST = []
numbers = (3,4,5,6)
print(numbers)
numbers2 = [3, 2, 3, 34,1, 'name']
print(numbers2)
numbers = [1, 2, 3, [numbers2]]
print(numbers)

name1 = 'Kesha'
name2 = 'popugay'
name3 = 'hui'
#OR
names4 = ['Kesha0', 'popugay1', 'hui2']
print(names4[1]) 
#INDEXES BEGINS FROM 0
print(names4[-1])

for name in names4:
    print(name)
# ЦИКЛ ФОР ИДЕТ ТОЛЬКО С ИН И ПЕЧАТАЕТ ПОСТРОЧНО КАЖДЫЙ ЭЛЕМЕНТ

#ПОЧЕМУ НЕ ДОБАВЛЯЕТ НЕСКОЛЬКО ИМЕН???Добавить в список имена
names4.append('Hulio99')
print(names4)
#Удалить из списка имена
names4.pop()
print(names4)
#Искать в списке по точному имени!!!
n = names4.index('popugay1')
print(n)
#Измерить длину списка!!!
print(len(names4))
#Сортировка чисел!!!!С добавлением функции по ПОСТРОЧНОМУ выводу результата по возрастанию...
sorting = [4,65,345,345,45,3,25,35,45,657,6,574,523,4,345,344,231,423]
for name in sorting:
    sorting.sort() #ИЛИ ПО УБЫВАНИЮ sorting.sort(reverse=True)
    print(name)
#ИЗМЕНЕНИЕ ЭЛЕМЕНТОВ СПИСКА
sorting[0] = 'S'
print(sorting)
#Если список состоит из разных типов переменных 
#БУКВЕННОГО ИЛИ ЦИФЕРНОГО ТО СОРТИРОВАТЬ НЕЛЬЗЯ