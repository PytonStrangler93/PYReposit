

def f(x):
    return x * 5


x = int(input())
l = []

while len(l) <= x - 1:
    l.append(int(input()))
print(l)

dictionary = {}
for i in l:
    if i in dictionary.keys():
        print(dictionary[i])
    else:
        dictionary[i] = f(i)
        print(dictionary[i])
