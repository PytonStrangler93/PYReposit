def solution(s):
    x = ''
    for i in s:
        if i.isupper():
            x += ' '+i
        else: x += i
    return x

def solution1(s):
    return ''.join(' ' + c if c.isupper() else c for c in s)

def solution2(s):
    return ''.join(i if i.islower() else ' ' + i for i in s)

print(solution("breakCamelCase"))