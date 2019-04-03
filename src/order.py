#!flask/bin/python
from time import time
import datetime
import os

import pandas as pd
import requests
from flask import Flask, request

# URL of the catalog server
CATALOG_SERVER = 'http://localhost:5000/'

# Initializing the book names as per the assignment
book_names = {'1': 'How to get a good grade in 677 in 20 minutes a day',
              '2': 'RPCs for Dummies',
              '3': 'Xen and the Art of Surviving Graduate School',
              '4': 'Cooking for the Impatient Graduate Student'}

# Initializing the available topics
topic_names = ['ds', 'gs']

app = Flask(__name__)

# Creating the log file along with starting the server
if not os.path.isfile('order_log.txt'):
    logs = open("order_log.txt", "x")
    logs.close()

# REST endpoint for buy
@app.route('/buy', methods=['GET'])
def buy_order():
    logs = open("order_log.txt", 'a')
    id = request.args.get('item', type=int)
    print('Querying for', book_names[str(id)])
    order_buy_start_time = time()
    r = requests.get(CATALOG_SERVER + 'query?item=' + str(id))
    print(r.json())
    if r.json()['books'][0]['stock'] > 0:
        b = requests.post(CATALOG_SERVER + 'update?item=' + str(id), json={'delta': -1})
        assert b.status_code == 200
        with open('./times/order_buy_time.txt', 'a') as f:
            f.write(str(time() - order_buy_start_time) + '\n')
        logs.write(str(datetime.datetime.now()) + ':Bought - ' + book_names[str(id)] + '\n')
        print('Bought ' + book_names[str(id)])
        return 'Bought ' + book_names[str(id)]
    else:
        with open('./times/order_buy_time.txt', 'a') as f:
            f.write(str(time() - order_buy_start_time) + '\n')
        logs.write(str(datetime.datetime.now()) + ':Out of Stock - ' + book_names[str(id)] + '\n')
        print('Out of Stock')
        return 'Out of Stock'


if __name__ == '__main__':
    df = pd.read_csv('sv_info.csv')
    CATALOG_SERVER = 'http://' + str(df['IP'][0]) + ':' + str(df['Port'][0]) + '/'
    ORDER_SERVER = 'http://' + str(df['IP'][1]) + ':' + str(df['Port'][1]) + '/'
    FRONTEND_SERVER = 'http://' + str(df['IP'][2]) + ':' + str(df['Port'][2]) + '/'

    app.run(host='0.0.0.0', port=df['Port'][1], debug=True)
