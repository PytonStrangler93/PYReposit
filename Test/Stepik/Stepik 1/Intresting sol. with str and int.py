

c = list(input())
z = [int(i) for i in c]
if sum(z[:3]) == sum(z[3:]):
    print("Счастливый")
else:
    print("Обычный")

a, b, c, d, e, f = (int(n) for n in input())
print(('Обычный', 'Счастливый')[a + b + c == d + e + f])


ans = {False: 'Счастливый', True: 'Обычный'}
b, c, d, e, f, g = (int(n) for n in input())
print(ans[bool((b + c + d) - (e + f + g))])
