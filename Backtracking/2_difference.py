def es(n: int, i: int, S: list[int]):
    if i < n:
        for k in range(1, 5):
            if i == 0 or abs(S[-1] - k) >= 2:
                S.append(k)
                es(n, i + 1, S)
                S.pop()
    else:
        print(S)


es(3, 0, [])
