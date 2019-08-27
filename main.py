from gemCalc import gem_calc
from collections import OrderedDict
from util import *
from pullGems import *


def main():

    total_gems, remainder, gems_in_results = 0, 0, 0
    ordered_list_of_gems = get_stash()
    gem_keys = list(ordered_list_of_gems.keys())
    gem_keys.remove(0)

    list_of_recipes = subsets_with_sum(gem_keys, 40, 6)
    num = get_key(ordered_list_of_gems, 0)
    list_of_recipes = sorted(list_of_recipes, key=lambda x:(x != num))

    results, remainder, remaining_gems = gem_calc(ordered_list_of_gems, list_of_recipes)

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


