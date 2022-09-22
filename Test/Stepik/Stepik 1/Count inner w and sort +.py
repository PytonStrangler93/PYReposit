with open('dataset_3363_3.txt', 'r') as f:
    n = f.read()


m = n.strip().split()  # строка в обычном регистре в список
b = n.lower().strip().split()  # строка в нижнем регистре в список


num = 0
for i in m:
    z = b.count(i.lower())
    if num < z:
        num = z

counts = []
for i in m:
    if b.count(i.lower()) == num:
        counts.append(i)

print(str(max(counts)) + ' ' + str(num))
