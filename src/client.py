import random
from time import sleep

import requests

CATALOG_SERVER = 'http://localhost:5000/'
ORDER_SERVER = 'http://localhost:5001/'
FRONTEND_SERVER = 'http://localhost:5002/'

actions = ['search', 'lookup', 'buy']
topics = ['ds', 'gs']

if __name__ == '__main__':

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
