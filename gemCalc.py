from util import *
from collections import OrderedDict


def gem_calc(ordered_list_of_gems, list_of_recipes):
    """
    Will take a OrderedDict of gemQuality:amount and an array containing gem recipes
    will sort the recipes in order of the top two largest buckets of gems
    returns the resulting dict of setOfGems:amount and the number of remaining gems
    :param ordered_list_of_gems: list of gems by quality number
    :param list_of_recipes: an array containing gem recipes
    :return: all recipes that will be required and how many times to use them
    """
    results = {}
    gems_to_remove = find_empty_buckets(ordered_list_of_gems)
    num_gems = sum(list(ordered_list_of_gems.values()))
    iteration_target = int(num_gems/3)

    for i in range(iteration_target):
        largest = get_key(ordered_list_of_gems, 0)
        second_largest = get_key(ordered_list_of_gems, 1)
        list_of_recipes.sort(key=lambda x:(largest not in x, second_largest not in x))

        if len(list_of_recipes) < 1:
            break
        j = list_of_recipes[0]
        for gem in gems_to_remove:
            if gem in j:
                list_of_recipes.pop(0)
                if len(list_of_recipes) < 1:
                    break
                j = list_of_recipes[0]
        if check_gems(ordered_list_of_gems, j):
            for k in j:
                if ordered_list_of_gems[int(k)] >= 1:
                    ordered_list_of_gems[int(k)] = ordered_list_of_gems[int(k)] - 1
            if str(j) not in results:
                results[str(j)] = 1
            elif str(j) in results:
                results[str(j)] += 1
            ordered_list_of_gems = OrderedDict(sorted(ordered_list_of_gems.items(), key=lambda t: t[1], reverse=True))
            gems_to_remove = find_empty_buckets(ordered_list_of_gems)

    results = OrderedDict(sorted(results.items(), key=lambda t: t[1], reverse=True))
    remaining_gems = sum(list(ordered_list_of_gems.values()))

    return results, remaining_gems, ordered_list_of_gems