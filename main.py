from gemCalc import gem_calc
from collections import OrderedDict
from util import *
from pullGems import pull_gems


def main():

    list_of_gems, results, remaining_gems = {}, {}, {}
    total_gems, remainder, gems_in_results = 0, 0, 0
    sess_id = input("Enter your Path Of Exile Session ID\n")
    temp_keys = []

    list_of_gems = pull_gems(sess_id)
    ordered_list_of_gems = OrderedDict(sorted(list_of_gems.items(), key=lambda t: t[1], reverse=True))
    print(sum(ordered_list_of_gems.values()))
    gem_keys = list(ordered_list_of_gems.keys())
    gem_keys.remove(0)

    list_of_recipes = subsets_with_sum(gem_keys, 40)
    print(list_of_recipes)
    num = getKey(ordered_list_of_gems, 0)
    list_of_recipes = sorted(list_of_recipes, key=lambda x:(x != num))
    print(list_of_recipes)

    temp = ordered_list_of_gems
    results, remainder, remaining_gems = gem_calc(temp, list_of_recipes)

    for k,v in results.items():
        temp_keys = k.strip('[]').split(', ')
        temp_keys = list(map(int, temp_keys))
        gems_in_results += (len(temp_keys)*v)
        temp_keys.sort(reverse=True)
        total_gems += (len(temp_keys) * v)
        print("Quality Gems Set", temp_keys, ':', v)

    print(remainder, "Gems Remaining")
    print(len(results), "different recipes")


if __name__ == "__main__":
    main()


