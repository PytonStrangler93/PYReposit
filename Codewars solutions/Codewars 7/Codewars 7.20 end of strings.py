# Complete the solution so that it returns true if the first argument(string) passed in ends with the 2nd argument (also a string).

# Examples:

# solution('abc', 'bc') # returns true
# solution('abc', 'd') # returns false

def solution(s, e):
    x = len(e)
    z = s[-x:]
    if z == e:
        return True
    elif x == 0:
        return True
    else:
        return False
    
def solution(string, ending):
   return string.endswith(ending)

def solution(string, ending):
    if string.endswith(ending):
        return True
    return False

def solution(a,b):
    return(a.endswith(b))

# str.endswith(suffix[, start[, end]])
# Метод str.endswith() возвращает True, если строка str заканчивается указанным суффиксом suffix, в противном случае возвращает False.