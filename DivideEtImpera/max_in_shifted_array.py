"""Si supponga di avere in input un vettore ordinato di n interi
     il cui contenuto `e stato ruotato di k posizioni.
     Supponendo di conoscere solo n, progettare un algoritmo
     che restituisca l’elemento massimo del vettore in O(log n) tempo."""

from collections import deque


def max_in_shifted_array(A: list[int], i: int, j: int) -> int:
    if A[i] < A[j]:
        return A[j]
    elif i == j:
        return A[i]
    m = i + ((j - i) // 2)
    if A[i] > A[m]:
        return max_in_shifted_array(A, i, m - 1)
    return max_in_shifted_array(A, m, j - 1)


A = [0, 1, 2, 3, 4, 5, 6]
k = 7
d = deque(A)
d.rotate(k)
A = list(d)
print(max_in_shifted_array(A, 0, len(A) - 1))
