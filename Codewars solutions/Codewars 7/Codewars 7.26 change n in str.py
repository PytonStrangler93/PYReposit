# Given a string of digits, you should replace any digit below 5 with '0' and any digit 5 and above with '1'. Return the resulting string.

# Note: input will never be an empty string

def fake_bin(x):
    return ''.join('0' if int(i) < 5 else '1' for i in x)
        


def fake_bin(x):
    result = ""
    for num in x:
        if int(num) < 5:
            result = result + "0"
        else:
            result = result + "1"
    return result

def fake_bin(x):
    return ''.join([str(int(i) // 5) for i in x])

fake_bin = lambda x: ''.join(['1','0'][e<'5'] for e in x)

def fake_bin(x):
    str_num = x
    for i in range(5):
        str_num = str_num.replace(str(i), "0")

    for i in range(5, 10):
        str_num = str_num.replace(str(i), "1")
        
    return str_num

def fake_bin(x):
    x = __import__('re').sub(r"[0-4]", "0", x)
    x = __import__('re').sub(r"[5-9]", "1", x)
    return x