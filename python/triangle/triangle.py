def equilateral(sides):
    a,b,c = sorted(sides)
    return (a > 0 and a+b > c) and a == c


def isosceles(sides):
    a,b,c = sorted(sides)
    return (a > 0 and a+b > c) and ((a == b) or (a == c) or (b == c))


def scalene(sides):
    a,b,c = sorted(sides)
    return (a > 0 and a+b > c) and ((a!=c) and (a!=b) and (b!=c))



