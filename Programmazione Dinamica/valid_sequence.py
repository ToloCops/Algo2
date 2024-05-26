def es1(S: list[int]):
    n = len(S)
    T = [0] * n
    for i in range(n):
        if i == 0 or i == 1:
            T[i] = S[i]
        else:
            T[i] = min(T[i - 1], T[i - 2]) + S[i]
    return min(T[-1], T[-2])


def es2(S):
    n = len(S)
    T = [[0, []] for _ in range(n)]
    for i in range(n):
        if i == 0 or i == 1:
            T[i] = [S[i], [S[i]]]
        else:
            T[i][0] = min(T[i - 1][0], T[i - 2][0]) + S[i]
            if T[i][0] == T[i - 1][0] - S[i]:
                T[i][1] = T[i - 1][1] + [S[i]]
            else:
                T[i][1] = T[i - 2][1] + [S[i]]
    return min(T[-1][0], T[-2][0]), T[-1][1] if T[-1][0] < T[-2][0] else T[-2][1]


S = [1, 2, 3, 5, 4, 6, 7]

print(es2(S))
