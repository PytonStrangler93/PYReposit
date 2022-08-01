# Trolls are attacking your comment section!

# A common way to deal with this situation is to remove all of the vowels from the trolls' comments, neutralizing the threat.

# Your task is to write a function that takes a string and return a new string with all vowels removed.

# For example, the string "This website is for losers LOL!" would become "Ths wbst s fr lsrs LL!".

# Note: for this kata y isn't considered a vowel.

def disemvowel(string_):
    return string_.translate({ord(i): None for i in 'aeiouAEIOU'})  # превращает символ из предложенного диапазона в пустоту.


def disemvowel(string):
    return "".join(c for c in string if c.lower() not in "aeiou") #то что я догадался без подсказок но не знал синтаксиса.



def disemvowel(s):
    for i in "aeiouAEIOU":
        s = s.replace(i,'')   #Меняет и на пустоту работает со строками
    return s

def disemvowel(string):
    return string.translate(None, 'aeiouAEIOU') # превращает символ из предложенного диапазона в пустоту.


import re

def disemvowel(string):
    return re.sub(r"[aeiouAEIOU]", "", string) #ХЗ че делает но свою работу выполняет
        
        
        