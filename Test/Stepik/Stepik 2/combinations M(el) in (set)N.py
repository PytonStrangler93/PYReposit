from math import factorial as f
# формула вхождения комбинаций  из М элементов в множество от 0 до N
# factorial(n)/(factorial(m)*factorial(n-m))

n, k = map(int, input().split())
res = int(f(n) / (f(k) * f(n - k)))
print(res)
