 #Return the number (count) of vowels in the given string.
#We will consider a, e, i, o, u as vowels for this Kata (but not y).
#The input string will only consist of lower case letters and/or spaces.



def get_count(sentence):
    return sum(sentence.count(v) for v in ['a', 'e', 'i', 'o', 'u'])  

def getCount(inputStr):
    return sum(1 for let in inputStr if let in "aeiouAEIOU")

def getCount(inputStr):
    num_vowels = 0
    for char in inputStr:
        if char in "aeiouAEIOU":
           num_vowels = num_vowels + 1
    return num_vowels

import re
def getCount(str):
    return len(re.findall('[aeiou]', str, re.IGNORECASE))

getCount = lambda s: sum(s.count(i) for i in 'aeiou')

def getCount(inputStr):
    num_vowels = 0
    # your code here
    for i in range (0, len(inputStr)):
        if (inputStr[i] == "a") or (inputStr[i] == "i") or (inputStr[i] == "u") or (inputStr[i] == "e") or (inputStr[i] == "o"):
            num_vowels = num_vowels + 1
    
    return num_vowels

