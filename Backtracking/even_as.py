def es(n: int, i: int, S: list[str], max_as: int, temp_as: int):
    if i < n:
        S.append("a")
        if temp_as + 1 >= max_as:
            es(n, i + 1, S, temp_as + 1, temp_as + 1)
        else:
            es(n, i + 1, S, max_as, temp_as + 1)
        S.pop()
        S.append("b")
        temp_as = 0
        es(n, i + 1, S, max_as, temp_as)
        S.pop()
    else:
        if max_as % 2 == 0:
            sequence = "".join(S)
            print(sequence)


es(100, 0, [], 0, 0)
