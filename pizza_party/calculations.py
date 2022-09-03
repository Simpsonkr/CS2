import math
def numberOfPizzas(people, slices):
    x=math.ceil((people*slices)/8)
    return x

def tax(x):
    y=x*.07
    return y

def delivery(x, y):
    z=(x+y)*.2
    return z
