# In this simple Kata your task is to create a function that turns a string into a Mexican Wave. 
# You will be passed a string and you must return that string in an array where an uppercase letter is a person standing up. 
# Rules
# 1.  The input string will always be lower case but maybe empty.
# 2.  If the character in the string is whitespace then pass over it as if it was an empty seat
# Example
# wave("hello") => ["Hello", "hEllo", "heLlo", "helLo", "hellO"]




def wave(people):
    my_list = []
    for i,j in enumerate(people):
        if j == ' ':
            pass
        else:
            my_list.append(people[:i] + people[i].capitalize()+ people[i+1:])
    return my_list

def wave1(str):
    return [str[:i] + str[i].upper() + str[i+1:] for i in range(len(str)) if str[i].isalpha()]
            