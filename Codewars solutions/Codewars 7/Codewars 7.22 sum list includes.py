# Sentence Smash
# Write a function that takes an array of words and smashes them together into a sentence and returns the sentence. You can ignore any need to sanitize words or add punctuation, but you should add spaces between each word. Be careful, there shouldn't be a space at the beginning or the end of the sentence!

# Example
# ['hello', 'world', 'this', 'is', 'great']  =>  'hello world this is great'

def smash(w):
    if len(w) == 0:
        return ''
    else:
        return ' '.join(w)
    
    
def smash(words):
    return " ".join(words)

# .join превращает список в строку и суммирует все значения "" перед .join это место где указывается что ставить между сложенными элеиендами списка.