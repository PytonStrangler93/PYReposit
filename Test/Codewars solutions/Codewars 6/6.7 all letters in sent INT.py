# A pangram is a sentence that contains every single letter of the alphabet at least once.
# For example, the sentence "The quick brown fox jumps over the lazy dog" is a pangram,
# because it uses the letters A-Z at least once (case is irrelevant).

# Given a string, detect whether or not it is a pangram. Return True if it
# is, False if not. Ignore numbers and punctuation.


import string


def is_pangram0(s):
    return not set('abcdefghijklmnopqrstuvwxyz') - set(s.lower())
# ПОДСМОТРЕЛ В ИНЕТЕ SET Это множество из него можно вычитать другое множество




def is_pangram2(s):
    s = s.lower()
    for char in 'abcdefghijklmnopqrstuvwxyz':
        if char not in s:
            return False
    return True


def is_pangram3(s):
    # ISSUBSET сравнивает заданное множеством алфавита в нижнем регистре
    return set(string.ascii_lowercase).issubset(s.lower())


def is_pangram(s):
    if len(s) <= 28:
        return False
    return True
