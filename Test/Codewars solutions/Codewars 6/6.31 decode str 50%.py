# Implement a pseudo-encryption algorithm which given a string S and an integer N concatenates 
# all the odd-indexed characters of S with all the even-indexed characters of S, this process should be repeated N times.
# Examples:
# encrypt("012345", 1)  =>  "135024"
# encrypt("012345", 2)  =>  "135024"  ->  "304152"
# encrypt("012345", 3)  =>  "135024"  ->  "304152"  ->  "012345"
# Together with the encryption function, you should also implement a decryption function which reverses the process.
# If the string S is an empty value or the integer N is not positive, return the first argument without changes.


def encrypt1(text, n):
    if text == '' or n <= 0 or text == None:
        return text
    else:
        odd = ''.join([text[i] for i in range(0, len(text)) if i % 2 != 0])
        even = ''.join([text[i] for i in range(0, len(text)) if i % 2 == 0])
        if n > 0:        
            return encrypt(odd+even, n-1)
        else:
            return odd+even

def decrypt(text, n):
    if text in ("", None):
        return text
    
    ndx = len(text) // 2

    for i in range(n):
        a = text[:ndx]
        b = text[ndx:]
        text = "".join(b[i:i+1] + a[i:i+1] for i in range(ndx + 1))
    return text



def encrypt(text, n):
    for i in range(n):
        text = text[1::2] + text[::2]
    return text





