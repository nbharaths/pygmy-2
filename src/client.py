import json
import random
from time import sleep

import pandas as pd
import requests

book_names = {'1': 'How to get a good grade in 677 in 20 minutes a day',
              '2': 'RPCs for Dummies',
              '3': 'Xen and the Art of Surviving Graduate School',
              '4': 'Cooking for the Impatient Graduate Student'}

actions = ['search', 'lookup', 'buy']
topics = ['ds', 'gs']


def pp_json(json_thing, sort=True, indents=4):
    if type(json_thing) is str:
        print(json.dumps(json.loads(json_thing), sort_keys=sort, indent=indents))
    else:
        print(json.dumps(json_thing, sort_keys=sort, indent=indents))
    return None


if __name__ == '__main__':

    df = pd.read_csv('sv_info.csv')
    CATALOG_SERVER = 'http://' + str(df['IP'][0]) + ':' + str(df['Port'][0]) + '/'
    ORDER_SERVER = 'http://' + str(df['IP'][1]) + ':' + str(df['Port'][1]) + '/'
    FRONTEND_SERVER = 'http://' + str(df['IP'][2]) + ':' + str(df['Port'][2]) + '/'

    while True:

        action = random.choice(actions)
        print(action)
        if action == 'search':
            topic = random.choice(topics)
            print('Starting a search for', topic)
            r = requests.get(FRONTEND_SERVER + 'search?topic=' + topic)
            print(r.status_code)
            assert r.status_code == 200, 'Search request failed!'
            pp_json(r.json())

        elif action == 'lookup':
            item = random.randint(1, 4)
            print('Starting a lookup for', book_names[str(item)])
            r = requests.get(FRONTEND_SERVER + 'lookup?item=' + str(item))
            print(r.status_code)
            assert r.status_code == 200, 'Lookup request failed!'
            pp_json(r.json())

        else:
            item = random.randint(1, 4)
            print('Trying to buy', book_names[str(item)])
            r = requests.get(FRONTEND_SERVER + 'buy?item=' + str(item))
            print(r.status_code)
            assert r.status_code == 200, 'Buy request failed!'
            print('Successfully bought', book_names[str(item)])

        sleep(5)
