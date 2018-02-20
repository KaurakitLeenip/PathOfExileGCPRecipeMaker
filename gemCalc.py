from util import *
from collections import OrderedDict

"""
Will take a OrderedDict of gemQuality:amount and an array containing sets that add to 40
will iterate over the recipes and remove the gems from the OrderedDict
returns the resulting dict of setOfGems:amount and the number of remaining gems

"""
def gemCalc( OrderedListOfGems, listOfRecipes ):

    tempArray = []
    results = {}
    numGems = sum(list(OrderedListOfGems.values()))
    iterationTarget = int(numGems/3)

    for i in range(iterationTarget):
        for j in listOfRecipes:
            if checkGems(OrderedListOfGems, j):
                for k in j:
                    if OrderedListOfGems[int(k)] >= 1:
                        OrderedListOfGems[int(k)] = OrderedListOfGems[int(k)] - 1
                if str(j) not in results:
                    results[str(j)] = 1
                elif str(j) in results:
                    results[str(j)] += 1
                OrderedListOfGems = OrderedDict(sorted(OrderedListOfGems.items(), key=lambda t: t[1], reverse=True))

    results = OrderedDict(sorted(results.items(), key=lambda t: t[1], reverse=True))
    remainingGems = sum(list(OrderedListOfGems.values()))


    return results, remainingGems, OrderedListOfGems