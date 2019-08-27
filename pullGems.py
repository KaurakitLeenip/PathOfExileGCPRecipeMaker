import requests
import json
from time import sleep
from collections import OrderedDict


POE_STASH_URL = 'https://pathofexile.com/character-window/get-stash-items?accountName=SerBubblez&league=Legion&tabIndex='
POE_NUM_TABS_URL = 'https://pathofexile.com/character-window/get-stash-items?accountName=SerBubblez&league=Legion&tabIndex=1&tabs=1'
SESSION_ID = ''

def get_stash():

    sess_id = input("Enter your Path Of Exile Session ID\n")
    list_of_gems = pull_gems(sess_id)
    ordered_list_of_gems = OrderedDict(sorted(list_of_gems.items(), key=lambda t: t[1], reverse=True))
    print(sum(ordered_list_of_gems.values()))

    return ordered_list_of_gems





def pull_gems(poe_session_id):
    """
    will use a session id to pull stash tab data from the poe website - json -> dictionary.
    iterates through all of it to pull gem data, leaving out level 20 gems as you probably dont want
    to use those for the recipe
    :param poe_session_id: session id from cookies that authenticates user
    :return: dictionary containing gem quality:amount
    """
    break_interval = 1
    list_of_gems = {}

    for i in range(20):
        list_of_gems[i] = 0

    sess_id = 'POESESSID=' + poe_session_id

    with requests.Session() as sess:
        i = 0
        headers = {'Cookie': sess_id}
        response = sess.post(POE_NUM_TABS_URL, headers=headers)
        content = json.loads(response.content)
        num_tabs = content["numTabs"]
        print(num_tabs, " total stash tabs")
        while i < num_tabs:
            url_string = POE_STASH_URL + str(i)
            response = sess.post(url_string, headers=headers)
            if response.status_code > 200:
                print(response.status_code, response.reason)
                sleepTime = 60 * break_interval
                break_interval += 1
                print("Being Throttled, please wait", sleepTime, "seconds")
                sleep(sleepTime)

            else:
                content = json.loads(response.content)
                for item in content['items']:
                    if 'Gem' in item['icon']:
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
