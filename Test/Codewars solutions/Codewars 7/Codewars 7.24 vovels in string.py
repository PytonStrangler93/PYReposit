# Trolls are attacking your comment section!

# A common way to deal with this situation is to remove all of the vowels
# from the trolls' comments, neutralizing the threat.

# Your task is to write a function that takes a string and return a new
# string with all vowels removed.

# For example, the string "This website is for losers LOL!" would become
# "Ths wbst s fr lsrs LL!".

# Note: for this kata y isn't considered a vowel.

import re


def disemvowel(string_):
    # превращает символ из предложенного диапазона в пустоту.
    return string_.translate({ord(i): None for i in 'aeiouAEIOU'})


def disemvowel(string):
    # то что я догадался без подсказок но не знал синтаксиса.
    return "".join(c for c in string if c.lower() not in "aeiou")


def disemvowel(s):
    for i in "aeiouAEIOU":
        s = s.replace(i, '')  # Меняет и на пустоту работает со строками
    return s


def disemvowel(string):
    # превращает символ из предложенного диапазона в пустоту.
    return string.translate(None, 'aeiouAEIOU')


def disemvowel(string):
    # ХЗ че делает но свою работу выполняет
    return re.sub(r"[aeiouAEIOU]", "", string)
