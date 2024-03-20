def es2n2(S, k):
    """
    Calculates the maximum number of zeros that can be obtained by splitting the list S into two parts,
    such that the sum of the elements in each part is less than or equal to k.

    Args:
        S (list): The input list of integers.
        k (int): The maximum sum allowed for each part.

    Returns:
        None
    """
    n = len(S)
    x_zeros = [0] * n
    y_zeros = [0] * n

    for i in range(n):
        if S[i] == 0:
            if i == 0: x_zeros[i] = 1
            else: x_zeros[i] = x_zeros[i-1] + 1
        else:
            if i == 0: x_zeros[i] = 0
            else: x_zeros[i] = x_zeros[i-1]

    for i in range(1, n+1):
        if S[-i] == 0:
            if -i == -1: y_zeros[i-1] = 1
            else: y_zeros[i-1] = y_zeros[i-2] +1
        else:
            if -i == -1: y_zeros[i-1] = 0
            else: y_zeros[i-1] = y_zeros[i-2]

    max_zeros = 0
    sum_x = 0
    for x in range(1, n + 1):
        max_y = n - 1 - x
        sum_x += S[x-1]
        sum_y = 0
        for y in range(1, max_y + 1):
            sum_y += S[-y]
            total_sum = sum_x + sum_y
            if total_sum <= k:
                zeros = x_zeros[x-1] + y_zeros[y-1]
                max_zeros = max(max_zeros, zeros)
    print("S: " + str(S))
    print("x_zeros: " + str(x_zeros))#prova
    print("y_zeros: " + str(y_zeros))
    print(max_zeros)
    return

S = [1, 0, 2, 8, 0, 5, 1, 6, 0, 0, 3]
k = 8



print(es2n2(S, k))