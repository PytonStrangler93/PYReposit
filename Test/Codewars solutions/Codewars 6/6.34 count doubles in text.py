

def duplicate_count(text):
    c = 0
    for i in set(list(text.lower())):
        if text.lower().count(i) > 1:
            c += 1
    return c

print(duplicate_count('abcdeaB'))

def duplicate_count1(s):
  return len([c for c in set(s.lower()) if s.lower().count(c)>1])