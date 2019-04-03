from time import time

import pandas as pd
import requests
from flask import Flask, request

book_names = {'1': 'How to get a good grade in 677 in 20 minutes a day',
              '2': 'RPCs for Dummies',
              '3': 'Xen and the Art of Surviving Graduate School',
              '4': 'Cooking for the Impatient Graduate Student'}

actions = ['search', 'lookup', 'buy']
topics = ['ds', 'gs']
app = Flask(__name__)


@app.route('/search', methods=['GET'])
def search():
    topic = request.args.get('topic', type=str)
    if topic is not None:
        print('Starting a search for topic', topic)
        frontend_search_start_time = time()
        r = requests.get(CATALOG_SERVER + 'query?topic=' + topic)
        with open('times/frontend_search_time.txt', 'a') as f:
            f.write(str(time() - frontend_search_start_time) + '\n')
        assert r.status_code == 200, 'Search failed!'

        return r.text


@app.route('/lookup', methods=['GET'])
def lookup():
    item_number = request.args.get('item', type=int)
    if item_number is not None:
        print('Starting a lookup for item', book_names[str(item_number)])
        frontend_lookup_start_time = time()
        r = requests.get(CATALOG_SERVER + 'query?item=' + str(item_number))
        with open('./times/frontend_lookup_time.txt', 'a') as f:
            f.write(str(time() - frontend_lookup_start_time) + '\n')
        return r.text


@app.route('/buy', methods=['GET'])
def buy():
    item_number = request.args.get('item', type=int)
    if item_number is not None:
        print('Starting a buy request for item', book_names[str(item_number)])
        frontend_buy_start_time = time()
        r = requests.get(ORDER_SERVER + 'buy?item=' + str(item_number))
        with open('./times/frontend_buy_time.txt', 'a') as f:
            f.write(str(time() - frontend_buy_start_time) + '\n')
        return r.text


if __name__ == '__main__':
    df = pd.read_csv('sv_info.csv')
    CATALOG_SERVER = 'http://' + str(df['IP'][0]) + ':' + str(df['Port'][0]) + '/'
    ORDER_SERVER = 'http://' + str(df['IP'][1]) + ':' + str(df['Port'][1]) + '/'
    FRONTEND_SERVER = 'http://' + str(df['IP'][2]) + ':' + str(df['Port'][2]) + '/'

    app.run(host='0.0.0.0', port=df['Port'][2], debug=True)
