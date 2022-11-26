# Jamie is a programmer, and James' girlfriend. She likes diamonds, and wants a diamond string from James. 
# Since James doesn't know how to make this happen, he needs your help.
# Task
# You need to return a string that looks like a diamond shape when printed on the screen, 
# using asterisk (*) characters. Trailing spaces should be removed, and every line must be terminated with a newline character (\n).
# Return null/nil/None/... if the input is an even number or negative, as it is not 
# possible to print a diamond of even or negative size.
# Examples
# A size 3 diamond:

#  *
# ***
#  *

def diamond(n):
    if n == None or n <= 0 or n % 2 == 0:
        return None
    else:
        x = ''.join(['{}{}'.format(' ' * ((n-len('*' * i))//2) ,(('*' * i) + '\n')) for i in range(1, n+1, 2)])
        y = ''.join(['{}{}'.format(' ' * ((n-len('*' * i))//2) ,(('*' * i) + '\n')) for i in range(n-2, 0, -2)])
        return   ''.join([x,y])

def diamond1(n):
    if n > 0 and n % 2 == 1:
        return ''.join(' ' * abs((n/2) - i) + '*' * (n - abs((n-1) - 2 * i)) + '\n' for i in range(n))
    return None

def diamond2(n):
    upDiamond = [ ' '*((n-r)/2) + '*'*r + '\n' for r in range(1, n+1, 2) ]
    return None if n%2 == 0 or n < 0 else ''.join(upDiamond + upDiamond[::-1][1:])


print(diamond(5))