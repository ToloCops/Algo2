import numpy as np


def min_insertions(S):
    n = len(S)

    # Create a table with all entries initialized to 0
    T = [[0 for _ in range(n)] for _ in range(n)]

    # Fill up the table
    for gap in range(1, n):
        i = 0
        for j in range(gap, n):
            if S[i] == S[j]:
                T[i][j] = T[i + 1][j - 1]
            else:
                T[i][j] = min(T[i][j - 1], T[i + 1][j]) + 1
            i += 1

    max_pal = 1

    # Return minimum number of insertions for S[0..n-1]
    for gap in range(1, n):
        i = 0
        for j in range(gap, n):
            if i != j and T[i][j] == 0:
                max_pal = max(j + 1 - i, max_pal)
            i += 1

    return T[0][n - 1], max_pal


S = "ciao"
print(min_insertions(S))
