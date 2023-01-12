import math

def manhattan_norm(x):
    return sum(map(abs,x))

def euclidean_norm(x):
    return math.sqrt(sum(map(lambda a:pow(a,2),x)))
