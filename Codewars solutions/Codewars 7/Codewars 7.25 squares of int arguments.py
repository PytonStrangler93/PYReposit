# Welcome. In this kata, you are asked to square every digit of a number and concatenate them.

# For example, if we run 9119 through the function, 811181 will come out, because 92 is 81 and 12 is 1.

# Note: The function accepts an integer and returns an integer


def square_digits(num):
    if num == 0:
        return 0
    else:
        z = str(num)
        a = z[0:1] 
        s = z[1:2]
        f = z[2:3]
        b = z[3:]
        c = int(a)**2
        v = int(s)**2
        h = int(f)**2
        j = int(b)**2
        k = str(c) + str(v) + str(h) + str(j)
        return int(k)
    
# самое тупое решение в истории человечества
    
    
def square_digits(num):
    ret = ""
    for x in str(num):
        ret += str(int(x)**2)
    return int(ret)

def square_digits(num):
    return int(''.join(str(int(d)**2) for d in str(num)))

def square_digits(num):
    result = 0
    multiplier = 1
    while num > 0:
        digit = (num % 10)
        result += (digit**2) * multiplier
        num /= 10
        multiplier *= 10
        if digit > 3:
            multiplier *= 10
    return result

def square_digits(n):
  return int("".join(str(pow(int(i), 2)) for i in str(n)))