import math
def perimeter(a, b, c):
    perimeter_length=a+b+c
    return perimeter_length

def find_area(s, a, b, c):
    holder=s*(s-a)
    holder=holder*(s-b)
    holder=holder*(s-c)
    area=math.sqrt(holder)
    return area
