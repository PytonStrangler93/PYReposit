#Implement a function which convert the given boolean value into its string representation.
#Note: Only valid inputs will be given.




def boolean_to_string(b):
    if b == True:
        return "True"
    else:
        return "False"
    
def boolean_to_string(b):
    return 'True' if b else 'False'

boolean_to_string = str  

def boolean_to_string(b):
    if b:
        return "True"
    return "False"

def boolean_to_string(b):
    return f"{b}"    