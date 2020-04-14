import requests
import json
from time import sleep
from util import *
from gemCalc import *


POE_STASH_URL = 'https://pathofexile.com/character-window/get-stash-items?accountName=SerBubblez&league=Legion&tabIndex=0'
POE_NUM_TABS_URL = 'https://pathofexile.com/character-window/get-stash-items?accountName=SerBubblez&league=Delirium&tabIndex=1&tabs=1'
SESSION_ID = ''

def gems(sess_id, max_recipe_length, league):

    total_gems, remainder, gems_in_results = 0, 0, 0
    ordered_list_of_gems = get_stash(sess_id, league)
    gem_keys = list(ordered_list_of_gems.keys())

    gem_set = []

    list_of_recipes = subsets_with_sum(gem_keys, 40, max_recipe_length)
    num = get_key(ordered_list_of_gems, 0)
    list_of_recipes = sorted(list_of_recipes, key=lambda x:(x != num))

    results, remainder, remaining_gems = gem_calc(ordered_list_of_gems, list_of_recipes)

    for k,v in results.items():
        temp_keys = k.strip('[]').split(', ')
        temp_keys = list(map(int, temp_keys))
        gems_in_results += (len(temp_keys)*v)
        temp_keys.sort(reverse=True)
        total_gems += (len(temp_keys) * v)
        gem_set.append("{0}: {1}".format(temp_keys, v))
        print("Quality Gems Set", temp_keys, ':', v)

    print(remainder, "Gems Remaining")
    print(len(results), "different recipes")

    return gem_set

def get_leagues():
    res = []
    league_url = "https://www.pathofexile.com/api/leagues"
    with requests.Session() as sess:
        response = sess.get(league_url)
        content = json.loads(response.content)
        for item in content:
            res.append(item['id'])
    return res


#get account name from /character-window/get-account-name
#add that to the stash url and num_tabs url
def get_stash(sess_id, league):

    list_of_gems = pull_gems(sess_id.strip())
    ordered_list_of_gems = OrderedDict(sorted(list_of_gems.items(), key=lambda t: t[1], reverse=True))
    return ordered_list_of_gems

def get_account_name(poe_session_id):
    url = "https://pathofexile.com/character-window/get-account-name"
    with requests.Session() as sess:
        headers = {'Cookie': "POESESSID=" + poe_session_id}
        response = sess.get(url, headers=headers)
        content = json.loads(response.content)
        acc_name = content['accountName']
        return acc_name


def pull_gems(poe_session_id):
    """
    will use a session id to pull stash tab data from the poe website - json -> dictionary.
    iterates through all of it to pull gem data, leaving out level 20 gems as you probably dont want
    to use those for the recipe
    :param poe_session_id: session id from cookies that authenticates user
    :return: dictionary containing gem quality:amount
    """
    list_of_gems = {}

    for i in range(1, 20):
        list_of_gems[i] = 0

    sess_id = 'POESESSID=' + poe_session_id
    url = 'https://pathofexile.com/character-window/get-stash-items?accountName={0}&league={1}&tabIndex='.format(get_account_name(poe_session_id), 'Standard')
    with requests.Session() as sess:
        i = 0
        headers = {'Cookie': sess_id}
        response = sess.post(POE_NUM_TABS_URL, headers=headers)
        content = json.loads(response.content)
        num_tabs = content["numTabs"]
        print(num_tabs, " total stash tabs")
        while i < 44:
            url_string = url + str(i)
            print(url_string)
            response = sess.get(url_string, headers=headers)
            if response.status_code > 200:
                print(response.status_code, response.reason)
                sleepTime = 60
                print("Being Throttled, please wait", sleepTime, "seconds")
                sleep(sleepTime)

            else:
                content = json.loads(response.content)
                for item in content['items']:
                    if 'Gem' in item['icon'] and 'properties' in item.keys():
                        for property in item['properties']:
                            if property['name'] == 'Level':
                                gemLevel = property['values'][0][0].split(" ")
                                gemLevel = int(gemLevel[0])
                            if property['name'] == 'Quality' and gemLevel != 20:
                                quality = int(property['values'][0][0].strip("+%"))
                                if quality < 20:
                                    list_of_gems[quality] += 1

                print("Pulled Stash ID ", i)
                i += 1

    print(list_of_gems)
    return list_of_gems
#print(get_leagues())
