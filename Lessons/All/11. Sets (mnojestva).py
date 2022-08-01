numbers = {1, 2, 4, 67}
print(numbers)

numbers2 = {} #Пустое множество вызвать нельзя это СЛОВАРЬ
print(type(numbers2))
#Чтобы вызвать пустое множество необходимо использовать спец команду
numbers2 = set() 
print(type(numbers2))
#Еще один из способов создать множество это когда мы берем еще какую-то структуру данных в качестве аргумента для нашей функции СЕТ
#Когда нужно вывести список с многими дублями так, чтобы дубли удалились.
numbers3 = set([1, 1, 2, 2, 4, 4]) 
print(numbers3)
#Обращение к элементу множества 
numbers4 = {1, 2, 3, 4, 5, 6, 7}
for i in numbers4:
    print(i)
#Как проверить входит ли какой-то єлемент в множество
numbers5 = {1, 2, 3, 4, 5, 6, 7}
print(3 in numbers5)
print(58 in numbers5)
numbers5.add(8)#Добавить что-то во множество
print(numbers5)
#Удалить что-то из множества 
numbers5.discard(8) #Если элемента нет не ругается если есть удаляет
print(numbers5)
numbers5.remove(7) #Если элеманта нет РУГАЕТСЯ если есть удаляет
print(numbers5)
numbers5.pop()#Удаляет только первый элемент
print(numbers5)
numbers5.clear()#Удаляет все элементы
print(numbers5)
#Обьединять множества!!
numbers4 = {1, 2, 3, 4, 5, 6, 7}
numbers6 = {8, 9, 10}
numbers7 = numbers4.union(numbers6) 
print(numbers7)
#Если мы обьединяем множества в которых есть одинаковые значение то в сумме дубли удаляются.
#Альтернативный символ |
numbers4 = {1, 2, 3, 4, 5, 6, 7}
numbers6 = {8, 9, 10}
numbers7 = numbers4 | numbers6
print(numbers7) 
#Удаление всего кроме дублирующихся значений
numbers9 = {1, 2, 3, 4, 5, 6, 7}
numbers10 = {1, 2, 3, 5, 7, 8, 9, 10}
numbers8 = numbers9.intersection(numbers10)
print(numbers8)
#ИЛИ АЛЬТЕРНАТИВНЫЙ СИМВОЛ
numbers9 = {1, 2, 3, 4, 5, 6, 7}
numbers10 = {1, 2, 3, 5, 7, 8, 9, 10}
numbers8 = numbers9 & numbers10
print(numbers8)
#РАЗНИЦА МЕЖДУ МНОЖЕСТВАМИ СОДЕРЖАТСЯ В ПЕРВОМ НО НЕ СОДЕРЖАТСЯ ВО ВТОРОМ И НАОБОРОТ ЕСЛИ ПОМЕНЯТЬ МЕСТАМИ
numbers99 = {3, 5, 7, 6, 4, 99, 12}
numbers98 = {12, 15, 6, 99, 14}
numbers97 = numbers98 - numbers99
print(numbers97) #Записал элементы которые находятся в 98 но не находятся в 99
#Копирует 
numbers99 = {3, 5, 7, 6, 4, 99, 12}
numbers98 = {12, 15, 6, 99, 14}
numbers97 = numbers98.copy()
print(numbers97)
#Показывает кол-во элементов в нашем множестве LEN
numbers99 = {3, 5, 7, 6, 4, 99, 12}
numbers98 = {12, 15, 6, 99, 14}
numbers97 = numbers98.copy()
print(len(numbers97))
#создание пустого множества которое нельзя изменить
numbers96 = frozenset({22, 33, 44, 55, 66, 77, 88})
print(numbers96)

