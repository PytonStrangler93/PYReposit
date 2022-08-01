# Given the triangle of consecutive odd numbers:

#              1
#           3     5
#        7     9    11
#    13    15    17    19
# 21    23    25    27    29
# ...
# Calculate the sum of the numbers in the nth row of this triangle (starting at index 1) e.g.: (Input --> Output)

# 1 -->  1
# 2 --> 3 + 5 = 8


def row_sum_odd_numbers(n):
    #your code here
    return n ** 3


def row_sum_odd_numbers(n):
    return sum(range(n*(n-1)+1, n*(n+1), 2))

def row_sum_odd_numbers(n):
    return n*n*n

def row_sum_odd_numbers(n):
    return pow(n, 3)

def row_sum_odd_numbers(n):
    #your code here
    a,b = n*(n-1)+1,n*(n+1)
    return sum(range(a,b,2)) if a != 1 else 1


# for x in range(1, n+1, 2):
#     print(x, end=' ')