#You get an array of numbers, return the sum of all of the positives ones.
#Example [1,-4,7,12] => 1 + 7 + 12 = 20
#Note: if there is nothing to sum, the sum is default to 0.



def positive_sum(arr):
    return sum(x for x in arr if x > 0)


def positive_sum(arr):
    sum = 0
    for e in arr:
        if e > 0:
            sum = sum + e
    return sum

def positive_sum(arr):
    return sum( max(i, 0) for i in arr )

def positive_sum(arr):
    return sum([i for i in arr if i==abs(i)])