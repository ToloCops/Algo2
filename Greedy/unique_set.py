def max_unique_set(G: list[list[tuple[int, int]]]) -> list[tuple[int, int]]:
    unique: list[tuple[int, int]] = []
    for n in G:
        heaviest: tuple[int, int] = (-1, -1)
        for arch in n:
            if heaviest[1] < arch[1]: heaviest = arch
        if heaviest[1] > 0: unique.append(heaviest)
    return unique

G: list[list[tuple[int, int]]] = [[(1, 2), (2, 3)],
      [(2, 1)],
      [],
      [(0, 1), (2, 4), (6, 5)],
      [(1, 2), (5, 8)],
      [(2, 8)],
      [(2, 7), (5, 3)]]  

print(max_unique_set(G))