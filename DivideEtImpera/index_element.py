def index_element(A: list[int], i: int, j: int) -> bool:
    if i == j and A[i] != i:
        return False
    m = (j + i) // 2
    if A[m] == m:
        return True
    elif A[m] < m:
        return index_element(A, m + 1, j)
    else:
        return index_element(A, i, m)


A = [0, 4, 5, 6, 7]

print(index_element(A, 0, len(A)))
