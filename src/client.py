import random
from time import sleep

import pandas as pd
import requests

actions = ['search', 'lookup', 'buy']
topics = ['ds', 'gs']

if __name__ == '__main__':

    df = pd.read_csv('sv_info.txt')
    CATALOG_SERVER = 'http://' + str(df['IP'][0]) + ':' + str(df['Port'][0]) + '/'
    ORDER_SERVER = 'http://' + str(df['IP'][1]) + ':' + str(df['Port'][1]) + '/'
    FRONTEND_SERVER = 'http://' + str(df['IP'][2]) + ':' + str(df['Port'][2]) + '/'


    while True:

        action = random.choice(actions)
        print(action)
        if action == 'search':
            topic = random.choice(topics)
            r = requests.get(FRONTEND_SERVER + 'search?topic=' + topic)
            print(r.status_code)

        elif action == 'lookup':
            item = random.randint(1, 4)
            r = requests.get(FRONTEND_SERVER + 'lookup?item=' + str(item))
            print(r.status_code)

        else:
            item = random.randint(1, 4)
            r = requests.get(FRONTEND_SERVER + 'buy?item=' + str(item))
            print(r.status_code)

        sleep(5)
