num = int(input())
divisor_counter = 0
number = 1
while number <= num:
    for i in range(1,num + 1):
        if number % i == 0:
            divisor_counter += 1
    print(str(number) + ('+' * divisor_counter))
    number += 1
    divisor_counter = 0