from math import sqrt

def es(n):
    bound = int(sqrt(n))+1
    count = 0
    for i in range(2, bound):
        if n % i == 0:
            count += 1
    return count == 1
