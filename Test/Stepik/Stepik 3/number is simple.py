from sympy import isprime

num_1, num_2 = int(input()), int(input())

for i in range(num_1, num_2 + 1):
    if isprime(i):
        print(i)