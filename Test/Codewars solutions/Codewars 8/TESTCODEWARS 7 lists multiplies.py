# Given a non-empty array of integers, return the result of multiplying the values together in order. Example:
# [1, 2, 3, 4] => 1 * 2 * 3 * 4 = 24
from functools import reduce
from operator import mul
import math as m


def grow(arr):
    return m.prod(arr)


def grow(arr):
    return reduce(lambda x, y: x * y, arr)


def grow(arr):
    return eval('*'.join([str(i) for i in arr]))


def grow(arr):
    return reduce(mul, arr, 1)


def grow(a): return __import__("functools").reduce(lambda x, y: x * y, a)
