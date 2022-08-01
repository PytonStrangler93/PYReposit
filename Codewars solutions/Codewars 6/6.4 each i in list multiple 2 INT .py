# Given an array of integers, return a new array with each value doubled.

# For example:

# [1, 2, 3] --> [2, 4, 6]

#ПОДСМОТРЕЛ В ИНЕТЕ КАДЫЙ ЭЛЕМЕНТ СПИСКА УМНОЖИТЬ НА 2

def maps(a):
    if a == []:
        return []
    else:
        return [i*2 for i in a]

print(maps([1, 2, 3]))

def maps(a):
    if len(a) > 0:
        for i in range(len(a)):
            a[i] = a[i] * 2
    return a


def maps(a):
    return list(map(lambda s: s*2, a))

def maps(a):
    b = list()
    for i in range(len(a)):
        b.append(a[i]*2)
    return b
    