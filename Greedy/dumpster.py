## Given a set of houses located in a street of a certain lenght, find the
## minimum number of dumpster in order to cover each house in range k



def place_dumpsters(L: list[int], k: int) -> list[int]:
    """
    Places dumpsters along a street based on the given list of house positions and the maximum distance between dumpsters.

    Args:
        L (list[int]): A list of house positions along the street.
        k (int): The maximum distance between dumpsters.

    Returns:
        list[int]: A list of dumpster positions.

    """
    dumpsters = []
    street = L[-1]
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