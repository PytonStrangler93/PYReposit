# КОРТЕЖИ Словари
# разница между списками и кортежем кортеж не изменяемый
tuple = ('first', 25, 25, 1,)
print(tuple)
# Кортеж обязательно заканчивается запятой
tuple = ('first',)
print(type(tuple))  # type позволяет вывести тип обьекта
# Кортеж в список и наоборот
# print(tuple([45, 47, 147, 45])) #Командой ТАПЛ в Кортеж
#print(list((45, 47, 147, 22)))
# Командой ЛИСТ в список
# СЛОВАРИ-контейнер для значений если в СПИСКАХ И КОРТЕЖАХ для индекса значения используется
# цифра то в словаре КЛЮЧ!! этот ключ может быть любого типа (Число буква
# и т.п.)
dict = {'apple': 'red', 'banana': 'yellow', 'lemon': 'yellow'}
print(dict)
# Для того чтобы вывести только ключи
for k in dict.keys():
    print(k)
# Для того чтобы вывести только значения
for k in dict.values():
    print(k)
# Для того чтобы вывести И КЛЮЧИ И ЗНАЧЕНИЯ
for k in dict.items():
    print(k)
# ИНТЕРЕСНЫЙ ФАКТ!!! Все выводится построчно через операторы такого типа.
# для того чтобы вывести конкретное значение пишем его ключ
print(dict['apple'])  # Ключ это слово с двоеточием
# Ключи менять можно!!! например
dict['banana'] = 'green'
print(dict['banana'])
# Из словаря можно что-то удалять командой ДЕЛ (если удаляется ключ
# удаляется и значение)
del (dict['banana'])
print(dict)
