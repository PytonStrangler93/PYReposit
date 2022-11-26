# The number 89 is the first integer with more than one digit that fulfills the property partially introduced in 
# the title of this kata. What's the use of saying "Eureka"? Because this sum gives the same number.
# In effect: 89 = 8^1 + 9^2
# The next number in having this property is 135.
# See this property again: 135 = 1^1 + 3^2 + 5^3
# We need a function to collect these numbers, that may receive two integers a, b that defines the range [a, b]
#  (inclusive) and outputs a list of the sorted numbers in the range that fulfills the property described above.
# Let's see some cases (input -> output):
# 1, 10 -> [1, 2, 3, 4, 5, 6, 7, 8, 9]
# 1, 100 -> [1, 2, 3, 4, 5, 6, 7, 8, 9, 89]
# If there are no numbers of this kind in the range [a, b] the function should output an empty list.
# 90, 100 --> []
# Enjoy it!!

def sum_dig_pow0(a, b): # range(a, b + 1) will be studied by the function
    v = []
    for i in range(a,b+1):
        if i < 10:
            v.append(i)
        else:
            z = []
            y = [int(x) for x in list(str(i))]
            n = [i for i in range(1,len(str(i))+1)]
            for x in range(0, len(str(i))):
                z.append(y[x]**n[x])
                if sum(z) == i:
                    v.append(sum(z)) 
    return v
###                
def dig_pow(n):
    return sum(int(x)**y for y,x in enumerate(str(n), 1))

def sum_dig_pow1(a, b): 
    return [x for x in range(a,b + 1) if x == dig_pow(x)]
###

def sum_dig_pow2(a, b):
    return [x for x in range(a, b+1) if sum(int(d)**i for i, d in enumerate(str(x), 1)) == x]

def sum_dig_pow3(a, b): # range(a, b + 1) will be studied by the function
    return [i for i in range(a,b+1) if i == sum(int(x)**(j+1) for j,x in enumerate(str(i)))]

def sum_dig_pow(a, b):
    return [n for n in range(a, b+1) if n == sum(int(dig) ** pow for pow, dig in enumerate(str(n), 1))]