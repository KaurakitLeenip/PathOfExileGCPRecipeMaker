from gemCalc import gemCalc
from collections import OrderedDict
from util import *
from subsetSum import *

def main():

    listOfGems, results, tResults, remainingGems, tRemainingGems = {}, {}, {}, {}, {}
    totalGems, tRemainder = 0, 0
    tKeys = []

    for i in range(1,21):
        quality = 21-i
        listOfGems[quality] = 0;


    inputStr = input("Please Enter CSV for Quality Gems descending from 20%\n")
    gems = inputStr.split(",")
    gems = list(map(int, gems))
    remainder = sum(gems)
    inputStr = input("1. For least remaining gems\n2. For least amount of recipes\n")

    for i in listOfGems:
        listOfGems[i] = gems[20-i]

    OrderedListOfGems = OrderedDict(sorted(listOfGems.items(), key=lambda t: t[1], reverse=True))
    print(sum(OrderedListOfGems.values()))
    gemKeys = list(OrderedListOfGems.keys())


    if inputStr == "1":
        listOfRecipes = subsets_with_sum(gemKeys, 40)
        num = getLargestGroup(OrderedListOfGems)
        listOfRecipes = sorted(listOfRecipes, key=lambda x:(x != num))

        temp = OrderedListOfGems
        tResults, tRemainder, tRemainingGems = gemCalc(temp, listOfRecipes)
        if tRemainder < remainder:
            results = tResults
            remainder = tRemainder
            remainingGems = tRemainingGems
            print(i)

        """listOfRecipes = subsetSum(gemKeys, 40)
        listOfRecipes.sort(key=lambda x:(x != list(OrderedListOfGems.keys())[0], x))


        temp = OrderedListOfGems
        tResults, tRemainder, tRemainingGems = gemCalc(temp, listOfRecipes)
        if tRemainder < remainder:
            results = tResults
            remainder = tRemainder
            remainingGems = tRemainingGems
            print(i)
        

    elif inputStr == "2":
        listOfRecipes = subsets_with_sum(gemKeys, 40)
        listOfRecipes.sort(key=len)

        tResults, tRemainder, tRemainingGems = gemCalc(OrderedListOfGems, listOfRecipes)
        if not bool(results):
            results = tResults
        if len(tResults) < len(results) and tRemainder < 80:
            remainingGems = tRemainingGems
            results = tResults
            remainder = tRemainder

        listOfRecipes = subsetSum(gemKeys, 40)
        listOfRecipes.sort(key=len)


        tResults, tRemainder, tRemainingGems = gemCalc(OrderedListOfGems, listOfRecipes)
        if len(tResults) < len(results):
            if tRemainder < 100:
                remainingGems = tRemainingGems
                results = tResults
                remainder = tRemainder
        """

    for k,v in results.items():
        tKeys = k.strip('[]').split(', ')
        tKeys = list(map(int, tKeys))
        tKeys.sort(reverse=True)
        totalGems += (len(tKeys) * v)
        print("Quality Gems Set", tKeys, ':', v)

        #print("Quality Gems Set", k, ":", v)
    print(remainder, "Gems Remaining")
    print(len(results), "different recipes")
    print(remainingGems)
    print(totalGems)

if __name__ == "__main__":
    main()


