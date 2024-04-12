def place_dumpsters(L: list[int], k: int) -> list[int]:
    dumpsters = []
    street = L[-1]
    #position = L[0]
    house = L[0]
    for i in range(k+1):
        if i == k or house + i == street:
            dumpsters.append(house+i)
            break

    for house in L:
        if house == L[0]: continue
        dump = dumpsters[-1]
        if house - dump > k:
            for i in range(k+1):
                if i == k or house + i == street:
                    dumpsters.append(house+i)
                    break
    return dumpsters
        

houses = [2, 5, 7, 11, 14, 16, 18]
k = 3 

print(place_dumpsters(houses, k))