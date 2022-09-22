stud = []
with open(r'D:\PYReposit\Test\Stepik\dataset_3363_4.txt', 'r', encoding="utf-8") as f:
    for string in f:
        x = string.strip().split(';')
        stud.append(x)

iterator = 0
sum_r = 0
sum_m = 0
sum_e = 0
for_write = []
for i in stud:
    grad_r = int(stud[stud.index(i)][1])
    grad_m = int(stud[stud.index(i)][2])
    grad_e = int(stud[stud.index(i)][3])
    for_write.append(str((grad_r + grad_m + grad_e) / 3))
    sum_r += grad_r
    sum_m += grad_m
    sum_e += grad_e
    iterator += 1

sum_list = [sum_r / iterator, sum_m / iterator, sum_e / iterator]


with open("HM2.txt", 'w') as w:
    for i in for_write:
        w.write(i + '\n')

    for i in sum_list:
        w.writelines(str(i) + ' ')
    w.close
