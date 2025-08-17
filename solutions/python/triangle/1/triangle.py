def equilateral(sides):
    a, b, c = sides
    return a == b == c and a != 0

def isosceles(sides):
    a, b, c = sides
    return (a == b or a == c or b == c) and a + b >= c and a + c >= b and b + c >= a

def scalene(sides):
    a, b, c = sides
    return a!=b and a!=c and b!=c and a + b >= c and a + c >= b and b + c >= a
