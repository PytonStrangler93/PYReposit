# If you can't sleep, just count sheep!!
# Task:
# Given a non-negative integer, 3 for example, return a string with a murmur: "1 sheep...2 sheep...3 sheep...". Input will always be valid, i.e. no negative integers.



def count_sheep(n):
    l = list(range(1, n+1))
    if n > 0:
        return ''.join(f'{i} sheep...' for i in l)
    else:
        return ''
#СНОВА СУКА НЕ МОЕ РЕШЕНИЕ!!!!!!!

def count_sheep(n):
    return ''.join(f"{i} sheep..." for i in range(1,n+1))

def count_sheep(n):
    sheep=""
    for i in range(1, n+1):
        sheep+=str(i) + " sheep..."
    return sheep

def count_sheep(n):
    if n == 1:
        return "1 sheep..."
    else:
        return count_sheep(n - 1) + "{} sheep...".format(n)