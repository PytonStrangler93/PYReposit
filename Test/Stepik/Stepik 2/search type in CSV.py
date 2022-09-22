# Вам дана частичная выборка из датасета зафиксированных преступлений, совершенных в городе Чикаго с 2001 года по настоящее время.
# Одним из атрибутов преступления является его тип – Primary Type.
# Вам необходимо узнать тип преступления, которое было зафиксировано максимальное число раз в 2015 году.


import csv


with open('Crimes.csv', 'r') as f:
    x = csv.reader(f)
    typec=[]
    for i in x:
        if '2015' in i[2]:
            typec.append(i[5])

most_comm = None
co = 0 
for i in set(typec):
    count = typec.count(i)
    if count > co:
        co = count
        most_comm = i

print(most_comm)
        