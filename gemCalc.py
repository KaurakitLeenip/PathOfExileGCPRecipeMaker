from util import *
from collections import OrderedDict

"""
Will take a OrderedDict of gemQuality:amount and an array containing sets that add to 40
will iterate over the recipes and remove the gems from the OrderedDict
returns the resulting dict of setOfGems:amount and the number of remaining gems

"""
def gemCalc( OrderedListOfGems, listOfRecipes ):

    results = {}
    gemsToRemove = findEmptyBuckets(OrderedListOfGems)
    numGems = sum(list(OrderedListOfGems.values()))
    iterationTarget = int(numGems/3)

    for i in range(500):
        largest = getKey(OrderedListOfGems, 0)
        secondLargest = getKey(OrderedListOfGems, 1)
        listOfRecipes.sort(key=lambda x:(largest not in x, secondLargest not in x))
        #print(OrderedListOfGems)
        #print(listOfRecipes)
        if len(listOfRecipes) < 1:
            break
        j = listOfRecipes[0]
        for gem in gemsToRemove:
            if gem in j:
                listOfRecipes.pop(0)
                if len(listOfRecipes) < 1:
                    break
                j = listOfRecipes[0]
        if checkGems(OrderedListOfGems, j):
            for k in j:
                if OrderedListOfGems[int(k)] >= 1:
                    OrderedListOfGems[int(k)] = OrderedListOfGems[int(k)] - 1
            if str(j) not in results:
                results[str(j)] = 1
            elif str(j) in results:
                results[str(j)] += 1
            OrderedListOfGems = OrderedDict(sorted(OrderedListOfGems.items(), key=lambda t: t[1], reverse=True))
            gemsToRemove = findEmptyBuckets(OrderedListOfGems)

    results = OrderedDict(sorted(results.items(), key=lambda t: t[1], reverse=True))
    remainingGems = sum(list(OrderedListOfGems.values()))

    return results, remainingGems, OrderedListOfGems