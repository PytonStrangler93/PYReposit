def modify_list(l):
    le = len(l) - 1
    i = le
    while i != -1:
        if l[i] % 2:
            del l[i]
        else:
            l[i] = l[i] // 2
        i -= 1
    return


def modify_list(l):
    l[:] = [i // 2 for i in l if not i % 2]


l = [1, 2, 3, 4, 5, 6]
print(modify_list(l))
print(l)
modify_list(l)
print(l)

# l = [10, 5, 8, 3]
# modify_list(l)
# print(l)
