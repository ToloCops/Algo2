def es(n: int, i: int, k: int, T: int, S: list[int]):
    if i < n:
        for j in range(k, -1, -1):
            if (n - i - 1) * k > T - j:
                S.append(j)
                es(n, i + 1, k, T - j, S)
                S.pop()
    else:
        if S[0] == 1:
            print(S)


es(6, 0, 4, 11, [])
