# Вам дано описание наследования классов исключений в следующем формате.
# <имя исключения 1> : <имя исключения 2> <имя исключения 3> ... <имя исключения k>
# Это означает, что исключение 1 наследуется от исключения 2, исключения 3, и т. д.
# Или эквивалентно записи:
# class Error1(Error2, Error3 ... ErrorK):
#     pass
# Антон написал код, который выглядит следующим образом.
# try:
#    foo()
# except <имя 1>:
#    print("<имя 1>")
# except <имя 2>:
#    print("<имя 2>")
# Костя посмотрел на этот код и указал Антону на то, что некоторые исключения можно не ловить, так как ранее в коде будет пойман их предок.
# Но Антон не помнит какие исключения наследуются от каких. Помогите ему выйти из неловкого положения и напишите программу, которая будет
# определять обработку каких исключений можно удалить из кода.
# Важное примечание:
# В отличие от предыдущей задачи, типы исключений не созданы.
# Создавать классы исключений также не требуется
# Мы просим вас промоделировать этот процесс, и понять какие из исключений можно и не ловить, потому что мы уже ранее где-то поймали их предка.
# Формат входных данных
# В первой строке входных данных содержится целое число n - число классов исключений.
# В следующих n строках содержится описание наследования классов. В i-й строке указано от каких классов наследуется i-й класс. Обратите внимание,
# что класс может ни от кого не наследоваться. Гарантируется, что класс не наследуется сам от себя (прямо или косвенно),
# что класс не наследуется явно от одного класса более одного раза.
# В следующей строке содержится число m - количество обрабатываемых исключений.
# Следующие m строк содержат имена исключений в том порядке, в каком они были написаны у Антона в коде.
# Гарантируется, что никакое исключение не обрабатывается дважды.
# Формат выходных данных
# Выведите в отдельной строке имя каждого исключения, обработку которого можно удалить из кода, не изменив при этом поведение программы.
# Имена следует выводить в том же порядке, в котором они идут во входных данных.
# Пример теста 1
# Рассмотрим код
# try:
#    foo()
# except ZeroDivision :
#    print("ZeroDivision")
# except OSError:
#    print("OSError")
# except ArithmeticError:
#    print("ArithmeticError")
# except FileNotFoundError:
#    print("FileNotFoundError")
# По условию этого теста, Костя посмотрел на этот код, и сказал Антону, что исключение FileNotFoundError
# можно не ловить, ведь мы уже ловим OSError -- предок FileNotFoundError
# Sample Input:
# 4
# ArithmeticError
# ZeroDivisionError : ArithmeticError
# OSError
# FileNotFoundError : OSError
# 4
# ZeroDivisionError
# OSError
# ArithmeticError
# FileNotFoundError
# Sample Output:
# FileNotFoundError

# МОЕ РЕШЕНИЕ НЕ ПРОПУСТИЛО!!!!!!!!!!!!!
import re
dict_constr = [input().replace(':', ' ').split() for i in range(int(input()))]
my_list = [input() for i in range(int(input()))]
my_dict = {}
for i in dict_constr:
    if len(i) == 1:
        my_dict[i[0]] = []
    else:
        my_dict[i[0]] = i[1:]

print(my_list)
print(dict_constr)
print(my_dict)
keys_set = []
for key in my_dict.keys():
    if len(my_dict[key]) > 0:
        ind_key = my_list.index(key)
        for i in my_dict[key]:
            inner_ind_key = my_list.index(i)
            if ind_key > inner_ind_key:
                keys_set.append(key)

for i in set(keys_set):
    if len(set(keys_set)) == 0:
        pass
    else:
        print(i)

# ИДЕАЛЬНО!!!!!


def checkdup(d):
    return cls[d] is None or any(map(checkdup, cls[d]))


cls = {d: set(b[1:]) for _ in range(int(input()))
       for d, *b in [input().split()]}

for _ in range(int(input())):
    c = input()
    if checkdup(c):
        print(c)
    cls[c] = None

# ДРУГИЕ РЕШЕНИЯ!!!!

# Функция разрешения соответствия


def finder(child, parent):
    if child == parent:
        return True
    for p in ancestors[child]:
        if finder(p, parent):
            return True
    return False


# Иерархия в словаре
ancestors = dict()
# Запись
for _ in range(int(input())):
    temp = input().split()
    ancestors[temp[0]] = temp[2:]
# Обработка
fin = []
for _ in range(int(input())):
    temp = input()
    for u in fin:
        if finder(temp, u):
            print(temp)
            break
    fin.append(temp)


d = {i.split()[0]: i.split()[2:] for i in [input()
                                           for _ in range(int(input()))]}

for k in d:
    for v in d[k]:
        d[k].extend(d[v])

b = []
for _ in range(int(input())):
    b.append(input())

for x in b:
    if x in d:
        for y in d[x]:
            if y in b and b.index(y) < b.index(x):
                print(x)
                break


def isParent(child, parent):
    return child == parent or any(
        map(lambda x: isParent(x, parent), dic[child]))


dic = {item[0]: item[1:]
       for item in [re.split("\\W+", input()) for _ in range(int(input()))]}
exc_l = [i for i in (input() for _ in range(int(input())))]

for i in range(len(exc_l)):
    if any(map(lambda x: isParent(exc_l[i], x), exc_l[:i])): print(exc_l[i])


def parent_checked(exception):
    return exception in checked or any(
        [parent_checked(p) for p in parents[exception]])

    # Развернутая версия сокращения выше

    # проверяем есть ли текущее исключение в списке тех что мы уже проверили
    # if exception in checked:
    #     return True

    # проверяем есть ли в списке проверенных исключений прямые предки (а затем и их прямые предки, а затем ...)
    # for el in parents[exception]:
    #     if parent_checked(el):
    #         return True

    # если так никого и не встретили выводит False - то есть предков еще не "поймали" - исключение нужно оставить
    # return False


n = int(input())
parents = {}

# Перебираем получаемые значения и формируем словарь {наследние : [родитель]}
for _ in range(n):
    a = input().split()
    parents[a[0]] = [] if len(a) == 1 else a[2:]

    # Развернутая версия сокращения выше
    # if a[0] not in parents.keys():
    #     parents[a[0]] = []
    # if len(a) > 1:
    #     parents[a[0]] += a[2:]

checked = set()
q = int(input())

for _ in range(q):
    e = input()
    # проверяем "поймали" ли мы исключение или его предков, если да печатаем
    # текущее исключение
    if parent_checked(e):
        print(e)
    # дополняем set проверенных исключений
    checked.add(e)


# put your python code here
ch_pars, s = {a[0]: a[2:] for a in [input().split() for _ in range(int(input()))]}, [
    [], []]  # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!


def find_parent(child):
    return 1 if child in s[0] else 0 if child not in ch_pars else any(
        map(find_parent, ch_pars[child]))


for a in [input() for _ in range(int(input()))]:
    s[find_parent(a)].append(a)
print(*s[1], sep='\n')
