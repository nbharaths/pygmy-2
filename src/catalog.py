#!flask/bin/python
import json
from time import time

import pandas as pd
from flask import Flask, jsonify, request

# Initializing the book names as per the assignment
book_names = {'1': 'How to get a good grade in 677 in 20 minutes a day',
              '2': 'RPCs for Dummies',
              '3': 'Xen and the Art of Surviving Graduate School',
              '4': 'Cooking for the Impatient Graduate Student'}

# Initializing the available topics
topic_names = ['ds', 'gs']

app = Flask(__name__)

# # Initializing the catalogs with the necessary details
books = [
    {
        'id': 1,
        'title': book_names['1'],
        'cost': 100,
        'topic': topic_names[0],
        'stock': 1500
    },
    {
        'id': 2,
        'title': book_names['2'],
        'cost': 200,
        'topic': topic_names[0],
        'stock': 1500
    },
    {
        'id': 3,
        'title': book_names['3'],
        'cost': 300,
        'topic': topic_names[1],
        'stock': 1500
    },
    {
        'id': 4,
        'title': book_names['4'],
        'cost': 400,
        'topic': topic_names[1],
        'stock': 1500
    }
]

# Initialising the persistent data
json.dump(books, open('catalog.json', 'w'))

# REST endpoint for query
@app.route('/query', methods=['GET'])
def get_books():
    books = json.load(open('catalog.json'))
    catalog_start_time = time()
    topic = request.args.get('topic', type=str)
    if topic is not None:  # query by subject
        ret = jsonify({'books': [b for b in books if b['topic'] == topic]})
        with open('./times/catalog_search_time.txt', 'a') as f:
            f.write(str(time() - catalog_start_time) + '\n')
        return ret

    id = request.args.get('item', type=int)
    if id is not None:  # query by item
        ret = jsonify({'books': [b for b in books if b['id'] == id]})
        with open('./times/catalog_lookup_time.txt', 'a') as f:
            f.write(str(time() - catalog_start_time) + '\n')
        return ret

# REST endpoint for update
@app.route('/update', methods=['POST'])
def update_books():
    books = json.load(open('catalog.json'))
    catalog_start_time = time()
    id = request.args.get('item', type=int)
    cost = request.json.get('cost')
    if cost is not None:  # query to update the cost of item
        for b in books:
            if b['id'] == id:
                b['cost'] = cost

    delta = request.json.get('delta')
    if delta is not None:  # query to update number of item
        for b in books:
            if b['id'] == id:
                b['stock'] += delta
    json.dump(books, open('catalog.json', 'w'))
    ret = jsonify({'books': [b for b in books if b['id'] == id]})
    with open('./times/catalog_buy_time.txt', 'a') as f:
        f.write(str(time() - catalog_start_time) + '\n')
    return ret


if __name__ == '__main__':
    df = pd.read_csv('sv_info.csv')
    CATALOG_SERVER = 'http://' + str(df['IP'][0]) + ':' + str(df['Port'][0]) + '/'
    ORDER_SERVER = 'http://' + str(df['IP'][1]) + ':' + str(df['Port'][1]) + '/'
    FRONTEND_SERVER = 'http://' + str(df['IP'][2]) + ':' + str(df['Port'][2]) + '/'

    app.run(host='0.0.0.0', port=df['Port'][0], debug=True)
