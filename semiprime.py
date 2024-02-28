from math import sqrt

def es(n):
    bound = int(sqrt(n))
    for i in range(2, bound):
        if n % i == 0:
            temp = n // i