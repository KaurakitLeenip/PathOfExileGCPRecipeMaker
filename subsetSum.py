from itertools import combinations_with_replacement

results = []

def subsetSum(numbers, target, partial=[]):

    s = sum(partial)
    # check if the partial sum is equals to target
    if s == target and len(partial) < 5:
        global results
        results.append(partial)
        #print ("sum(%s)=%s" % (partial, target))

    if s >= target:
        return  # if we reach the number why bother to continue

    for i in range(len(numbers)):
        n = numbers[i]
        remaining = numbers[i+1:]
        subsetSum(remaining, target, partial + [n])

    return results

def subsets_with_sum(lst, target):
    x = 0
    def _subset(idx, l, results, target):
        if target == sum(l) and len(l) < 5:
            results.append(l)
        elif target < sum(l):
            return
        for i in range(idx, len(lst)):
            _subset(i, l + [lst[i]], results, target)
        return results
    return _subset(0, [], [], target)
