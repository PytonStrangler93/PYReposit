from re import X


def greet(x):
    if x == ('Hello world'):
        return x
    else: 
        return 'Hello world'
    
def greet():
    poem = []
    
    poem.append("h is for happy")
    poem.append("e is for energy")
    poem.append("l is for love")
    poem.append("l is also for life")
    poem.append("o is for original like this poem")
    poem.append(" ")
    poem.append("w is for your well-being")
    poem.append("o is for optimism which we all should have")
    poem.append("r is for rest which we all need more")
    poem.append("l is longing for a better future")
    poem.append("d is a deep-felt thanks for reading this poem")
    poem.append("! <3<3<3")
    
    return ''.join(p[0] for p in poem)
