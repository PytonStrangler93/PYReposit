


def descending_order(num):    
    return int(''.join(map(str, sorted([int(i) for i in str(num)])[::-1])))

def Descending_Order(num):
    return int(''.join(sorted(list(str(num)), reverse=True)))

Descending_Order = lambda n: int(''.join(reversed(sorted(str(n)))))

print(descending_order(123456789))