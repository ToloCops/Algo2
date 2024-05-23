def es(n: int, i: int, S: list[str], num_as: int, num_bs: int):
    if n % 2 == 1:
        return
    if i < n:
        if n - i == 1 and num_as % 2 == 1:
            pass
        else:
            S.append("a")
            es(n, i + 1, S, num_as + 1, num_bs)
            S.pop()
        if n - i == 1 and num_bs % 2 == 1:
            pass
        else:
            S.append("b")
            es(n, i + 1, S, num_as, num_bs + 1)
            S.pop()
    else:
        sequence = "".join(S)
        print(sequence)


def es2(n: int, i: int, S: list[str], num_as: int, num_bs: int):
    if n % 2 == 1:
        return
    if i < n:
        if num_as % 2 == 0 or n - i != 1:
            S.append("a")
            es(n, i + 1, S, num_as + 1, num_bs)
            S.pop()
        if num_bs % 2 == 0 or n - i != 1:
            S.append("b")
            es(n, i + 1, S, num_as, num_bs + 1)
            S.pop()
    else:
        sequence = "".join(S)
        print(sequence)


es2(4, 0, [], 0, 0)
