from math import sqrt

def es(n):
    """
    Check if a number is a semiprime.

    A semiprime is a number that is the product of two prime numbers.

    Parameters:
    n (int): The number to check.

    Returns:
    bool: True if the number is a semiprime, False otherwise.
    """
    bound = int(sqrt(n))+1
    count = 0
    for i in range(2, bound):
        if n % i == 0:
            count += 1
    return count == 1
