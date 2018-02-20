"""
checks if a set of gems exists in an orderedDict of
gems


"""
def checkGems(OrderedListOfGems, arrayOfGems):

    exists = True

    for i in arrayOfGems:
        if not i in OrderedListOfGems or OrderedListOfGems[i] == 0:
            exists = False

    return exists

"""
gets the gem quality with the lowest amount
"""
def getLowestNum(OrderedListOfGems, arrayOfGems):

    lowest = float('inf')
    arrayOfGems = list(map(int, arrayOfGems))


    for i in arrayOfGems:
        if OrderedListOfGems[i] < lowest:
            lowest = OrderedListOfGems[i]

    return lowest

def getLargestGroup(OrderedListOfGems):
    arr = list(OrderedListOfGems.keys())
    return arr[0]