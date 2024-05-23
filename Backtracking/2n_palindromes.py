def es(n: int, i: int, S: list[str]):
    if i < n:
        S.append("a")
        es(n, i + 1, S)
        S.pop()
        S.append("b")
        es(n, i + 1, S)
        S.pop()
    else:
        B = S.copy()
        B.reverse()
        S = S + B
        sequence = "".join(S)
        print(sequence)


es(2, 0, [])
