import random
from time import sleep

import requests

CATALOG_SERVER = 'http://localhost:5000/'
ORDER_SERVER = 'http://localhost:5001/'

actions = ['search', 'lookup', 'buy']
topics = ['ds', 'gs']


def search(topic):
    r = requests.get(CATALOG_SERVER + 'query?topic=' + topic)
    print(r.text)


def lookup(item_number):
    r = requests.get(CATALOG_SERVER + 'query?item=' + str(item_number))
    print(r.text)


def buy(item_number):
    r = requests.get(ORDER_SERVER + 'buy?item=' + str(item_number))
    print(r.text)


if __name__ == '__main__':

    while True:

        action = random.choice(actions)
        print(action)
        if action == 'search':
            topic = random.choice(topics)
            search(topic)

        elif action == 'lookup':
            item = random.randint(1, 4)
            lookup(item)

        else:
            item = random.randint(1, 4)
            buy(item)

        sleep(5)
