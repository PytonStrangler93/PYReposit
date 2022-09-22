# В этой задаче вам необходимо воспользоваться API сайта numbersapi.com
# Вам дается набор чисел. Для каждого из чисел необходимо узнать, существует ли интересный математический факт об этом числе.
# Для каждого числа выведите Interesting, если для числа существует интересный факт, и Boring иначе.
# Выводите информацию об интересности чисел в таком же порядке, в каком следуют числа во входном файле.
# Пример запроса к интересному числу:
# http://numbersapi.com/31/math?json=true
# Пример запроса к скучному числу:
# http://numbersapi.com/999/math?json=true
# Пример входного файла:
# 31
# 999
# 1024
# 502
# Пример выходного файла:
# Interesting
# Boring
# Interesting
# Boring


import requests

with open('dataset_24476_3.txt', 'r') as f:
    x = map(int, f.read().strip().split())
    
a = []
for i in x:
    url = f'http://numbersapi.com/{i}/math?json=true'
    req = requests.get(url)
    res = req.json() #== json.loads(req.text)
    if res['found'] == True:
        a.append('Interesting')
    else:
        a.append('Boring')
        
for i in a:
    with open("text.txt", 'a') as x:
        x.write(i+'\n')
    