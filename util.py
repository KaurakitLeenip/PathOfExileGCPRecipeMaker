def check_gems(ordered_list_of_gems, array_of_gems):
    """
    checks if a set of gems exists in an orderedDict of
    gems
    :param ordered_list_of_gems: list of gems by quality number
    :param array_of_gems: recipe to
    :return: bool if item exists
    """
    exists = True

    for i in array_of_gems:
        if i not in ordered_list_of_gems or ordered_list_of_gems[i] == 0:
            exists = False

    return exists

def get_key(ordered_list_of_gems, index):
    """
    gets a indexed value from an OrderedDict
    :param ordered_list_of_gems: list of gems by quality number
    :param index: index number to return value of
    :return: gem quality at that index
    """
    arr = list(ordered_list_of_gems.keys())
    return arr[index]


def find_empty_buckets(ordered_list_of_gems):
    """
    find the quality categories that are empty
    :param ordered_list_of_gems: list of gems by quality number
    :return: gem qualities that have no items
    """
    gems_to_remove = []
    for key, value in ordered_list_of_gems.items():
        if value == 0:
            gems_to_remove.append(key)

    return gems_to_remove


def subsets_with_sum(lst, target, set_size):
    """
    finds all subsets of a set of numbers which sum up to a target
    :param lst: list of gem qualities
    :param target: the target number to add up to
    :param set_size: the max number of gems in a recipe
    :return: recursive call
    """
    x = 0
    results = []

    def _subset(idx, l, results, target):
        if target == sum(l) and len(l) < set_size-1:
            results.append(l)
        elif target < sum(l):
            return
        for i in range(idx, len(lst)):
            _subset(i, l + [lst[i]], results, target)
        return results
    return _subset(0, [], [], target)