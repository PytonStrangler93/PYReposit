#Given a non-empty array of integers, return the result of multiplying the values together in order. Example:
#[1, 2, 3, 4] => 1 * 2 * 3 * 4 = 24
import math as m

def grow(arr):
    return m.prod(arr)

from functools import reduce

def grow(arr):
    return reduce(lambda x, y: x * y, arr)

def grow(arr):
    return eval('*'.join([str(i) for i in arr]))

from functools import reduce
from operator import mul

def grow(arr):
    return reduce(mul, arr, 1)

grow = lambda a: __import__("functools").reduce(lambda x,y: x*y, a)
