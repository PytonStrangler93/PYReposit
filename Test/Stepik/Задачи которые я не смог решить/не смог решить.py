# Вам дано описание наследования классов в следующем формате.
# <имя класса 1> : <имя класса 2> <имя класса 3> ... <имя класса k>
# Это означает, что класс 1 отнаследован от класса 2, класса 3, и т. д.
# Или эквивалентно записи:
# class Class1(Class2, Class3 ... ClassK):
#     pass
# Класс A является прямым предком класса B, если B отнаследован от A:
# class B(A):
#     pass
# Класс A является предком класса B, если
# A = B;
# A - прямой предок B
# существует такой класс C, что C - прямой предок B и A - предок C
# Например:
# class B(A):
#     pass
# class C(B):
#     pass
# # A -- предок С
# Вам необходимо отвечать на запросы, является ли один класс предком другого класса
# Важное примечание:
# Создавать классы не требуется.
# Мы просим вас промоделировать этот процесс, и понять существует ли путь от одного класса до другого.
# Формат входных данных
# В первой строке входных данных содержится целое число n - число классов.
# В следующих n строках содержится описание наследования классов. В i-й строке указано от каких классов наследуется i-й класс. Обратите внимание, что класс может ни от кого не наследоваться. Гарантируется, что класс не наследуется сам от себя (прямо или косвенно), что класс не наследуется явно от одного класса более одного раза.
# В следующей строке содержится число q - количество запросов.
# В следующих q строках содержится описание запросов в формате <имя класса 1> <имя класса 2>.
# Имя класса – строка, состоящая из символов латинского алфавита, длины не более 50.
# Формат выходных данных
# Для каждого запроса выведите в отдельной строке слово "Yes", если класс 1 является предком класса 2, и "No", если не является.
# Sample Input:
# 4
# A
# B : A
# C : A
# D : B C
# 4
# A B
# B D
# C D
# D A
# Sample Output:
# Yes
# Yes
# Yes
# No


n = int(input())

parents = {}
for _ in range(n):
    a = input().split()
    parents[a[0]] = [] if len(a) == 1 else a[2:]


def is_parent(child, parent):
    return child == parent or any(
        map(lambda p: is_parent(p, parent), parents[child]))


q = int(input())
for _ in range(q):
    a, b = input().split()
    print("Yes" if is_parent(b, a) else "No")


def test(parent, child):
    if parent == child or parent in base[child]:
        return 'Yes'
    for i in base[child]:
        if test(parent, i) == 'Yes':
            return 'Yes'
    return 'No'


base = {}
for com in [input().split(' ') for i in range(int(input()))]:
    base[com[0]] = com[2:len(com)]
for com in [input().split(' ') for i in range(int(input()))]:
    print(test(com[0], com[1]))


def isP(pr, ch):
    return ch == pr or any(map(lambda pl: isP(pr, pl), p[ch]))


p = {}
for j in range(2):
    for c in [input().split() for i in range(int(input()))]:
        if j:
            print(['No', 'Yes'][isP(*c)])
        else:
            p[c[0]] = c[2:]


# put your python code here
def find_path(start, path):
    path.add(start)
    for node in graph[start]:
        if node not in path:
            find_path(node, path)


graph = {}
for i in range(int(input())):
    s = input().split()
    graph[s[0]] = s[2:] if len(s) > 1 else [s[0]]

for i in range(int(input())):
    s = input().split()
    path = set()
    find_path(s[1], path)
    print('Yes' if s[0] in path else 'No')


inheritance = dict()
for i in [input().split() for _ in range(int(input()))]:
    inheritance[i[0]] = i[2:]
for k, v in inheritance.items():
    for i in v:
        if i in inheritance:
            inheritance[k].extend(inheritance[i])
for parent, inheritor in [input().split() for _ in range(int(input()))]:
    print(['No', 'Yes'][parent == inheritor or parent in inheritance[inheritor]])


# с рекурсией. Дословано по заданию.

clas = {}  # словарь наследник : предки


def find_cls(A, B):
    if A == B:  # если A = B
        return True
    elif A in clas[B]:  # если А прямой предок В
        return True
    else:
        for C in clas[B]:  # если есть С прямой предок В и, не обязательно прямой, но предок А
            if find_cls(A, C):
                return True
        return False


for _ in range(int(input())):  # заполняем словарь
    inp = str(input()).split()
    # хотел делать через множество на случай пересоздания класса. Не
    # реализовал и не пригодилось
    clas.update({inp[0]: set(inp[2:])})

for _ in range(int(input())):  # проверяем классы через функцию
    inp = (str(input()).split())
    cls1, cls2 = inp[0], inp[1]
    if find_cls(cls1, cls2):
        print("Yes")
    else:
        print("No")
