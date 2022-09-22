a, b = input().split()
a = int(a)
b = int(b)
#s = 0
spisok = []
for i in range(a, b + 1):
    if i % 3 == 0:
        spisok.append(i)
        # s+=i
print(sum(spisok) / len(spisok))
