#Given an array of ones and zeroes, convert the equivalent binary value to an integer.
#Eg: [0, 0, 0, 1] is treated as 0001 which is the binary representation of 1.
#Examples:
#Testing: [0, 0, 0, 1] ==> 1
#Testing: [0, 0, 1, 0] ==> 2
#Testing: [0, 1, 0, 1] ==> 5
#Testing: [1, 0, 0, 1] ==> 9
#Testing: [0, 0, 1, 0] ==> 2
#Testing: [0, 1, 1, 0] ==> 6
#Testing: [1, 1, 1, 1] ==> 15
#Testing: [1, 0, 1, 1] ==> 11
#However, the arrays can have varying lengths, not just limited to 4.
#>>> bin(123) Перевод в бинарную систему
#'0b1111011'
#>>> int('1111011', 2) перевод в двоичную систему
#123

def x(z):
    h = ''.join(map(str, z))
    return int(h, 2)

def binary_array_to_number(arr):
    return int("".join(map(str, arr)), 2)

def binary_array_to_number(arr):
    return int(''.join(str(a) for a in arr), 2)      

def binary_array_to_number(arr):
    s = 0
    for digit in arr:
        s = s * 2 + digit

    return s

def binary_array_to_number(arr):
    return sum(digit * 2**i for i, digit in enumerate(reversed(arr)))  

def binary_array_to_number(arr):
  no_of_elements = len(arr)
  k = no_of_elements 
  sum = 0
  while k != 0:
      sum = sum + arr[no_of_elements-k]*(2**(k-1))
      k = k - 1
  return sum