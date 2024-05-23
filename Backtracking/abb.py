def es(n: int, i: int, S: list[str], timer: int):
    if i < n:
        if timer == 0 and n - i > 2:
            S.append("a")
            es(n, i + 1, S, 2)
            S.pop()
        S.append("b")
        if timer != 0:
            es(n, i + 1, S, timer - 1)
        else:
            es(n, i + 1, S, timer)
            S.pop()
            S.append("c")
            es(n, i + 1, S, timer)
        S.pop()
    else:
        print(S)


def es2(n: int, i: int, S: list[str]):
    if i < n:
        for e in ["a", "b", "c"]:
            if e == "a":
                if i + 3 <= n:
                    S += ["a", "b", "b"]
                    es2(n, i + 3, S)
                    S.pop()
                    S.pop()
                    S.pop()
            else:
                S.append(e)
                es2(n, i + 1, S)
                S.pop()
    else:
        print(S)


es2(4, 0, [])
