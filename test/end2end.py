import json
import os
import random
from time import sleep, time

import pandas as pd
import requests

# Initializing the book names as per the assignment
book_names = {'1': 'How to get a good grade in 677 in 20 minutes a day',
              '2': 'RPCs for Dummies',
              '3': 'Xen and the Art of Surviving Graduate School',
              '4': 'Cooking for the Impatient Graduate Student'}

# Initializing the available actions
actions = ['search', 'lookup', 'buy']
# Initializing the available topics
topics = ['ds', 'gs']


# Pretty printing for json
def pp_json(json_thing, sort=True, indents=4):
    if type(json_thing) is str:
        print(json.dumps(json.loads(json_thing), sort_keys=sort, indent=indents))
    else:
        print(json.dumps(json_thing, sort_keys=sort, indent=indents))
    return None


def test_out_of_stock():
    print("*** Testing out of stock case ***")
    df = pd.read_csv('sv_info.csv')

    FRONTEND_SERVER = 'http://' + str(df['IP'][2]) + ':' + str(df['Port'][2]) + '/'

    # testing buying the stock item
    print("Buying a book for 5 times")
    for _ in range(5):
        print('Trying to buy', book_names[str(1)])
        r = requests.get(FRONTEND_SERVER + 'buy?item=' + str(1))
        file = open("../src/order_log.txt")
        lines = file.readlines()
        if "Bought" in lines[-1]:
            print("Buy Successful")
        else:
            print("Test case failed")

    # testing buying the updated stock item
    print("Buying now should fail")
    print('Trying to buy', book_names[str(1)])
    r = requests.get(FRONTEND_SERVER + 'buy?item=' + str(1))
    file = open("../src/order_log.txt")
    lines = file.readlines()
    if "Out of Stock" in lines[-1]:
        print("Buying failed")
        print("!!! Test passed !!!")
    else:
        print("!!! Test failed !!!")


def test_restock():
    print("*** Testing restock case ***")
    df = pd.read_csv('sv_info.csv')

    CATALOG_SERVER = 'http://' + str(df['IP'][0]) + ':' + str(df['Port'][0]) + '/'
    ORDER_SERVER = 'http://' + str(df['IP'][1]) + ':' + str(df['Port'][1]) + '/'
    FRONTEND_SERVER = 'http://' + str(df['IP'][2]) + ':' + str(df['Port'][2]) + '/'

    # testing buying the item
    print("Buying a book for 5 times")
    for _ in range(5):
        print('Trying to buy', book_names[str(1)])
        r = requests.get(FRONTEND_SERVER + 'buy?item=' + str(1))
        file = open("../src/order_log.txt")
        lines = file.readlines()
        if "Bought" in lines[-1]:
            print("Buy Successful")
        else:
            print("Test case failed")

    # testing buying the out of stock item
    print("Buying now should fail")
    print('Trying to buy', book_names[str(1)])
    r = requests.get(FRONTEND_SERVER + 'buy?item=' + str(1))
    file = open("../src/order_log.txt")
    lines = file.readlines()
    if "Out of Stock" in lines[-1]:
        print("Buying failed")
    else:
        print("!!! Test failed !!!")

    # Updating the stock of the out of stock product
    b = requests.post(CATALOG_SERVER + 'update?item=' + str(1), json={'delta': 2})
    assert b.status_code == 200, 'Periodic update failed!'
    print('Periodic update successful for', book_names[str(1)])

    # testing buying the updated stock item
    print("Buying now should succeed")
    print('Trying to buy', book_names[str(1)])
    r = requests.get(FRONTEND_SERVER + 'buy?item=' + str(1))
    file = open("../src/order_log.txt")
    lines = file.readlines()
    if "Bought" in lines[-1]:
        print("Bought successfully")
        print("!!! Test passed !!!")
    else:
        print("!!! Test failed !!!")


def main():
    # Uncomment the test that you want to run.
    # Please make sure to start a fresh catalog server for each end to end test

    # test_out_of_stock()

    test_restock()


if __name__ == '__main__':
    main()
