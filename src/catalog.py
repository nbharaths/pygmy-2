#!flask/bin/python
import pandas as pd
from flask import Flask, jsonify, request

book_names = {'1': 'How to get a good grade in 677 in 20 minutes a day',
              '2': 'RPCs for Dummies',
              '3': 'Xen and the Art of Surviving Graduate School',
              '4': 'Cooking for the Impatient Graduate Student'}

topic_names = ['ds', 'gs']

app = Flask(__name__)

books = [
    {
        'id': 1,
        'title': book_names['1'],
        'cost': 100,
        'topic': topic_names[0],
        'stock': 10
    },
    {
        'id': 2,
        'title': book_names['2'],
        'cost': 200,
        'topic': topic_names[0],
        'stock': 10
    },
    {
        'id': 3,
        'title': book_names['3'],
        'cost': 300,
        'topic': topic_names[1],
        'stock': 10
    },
    {
        'id': 4,
        'title': book_names['4'],
        'cost': 400,
        'topic': topic_names[1],
        'stock': 10
    }
]


@app.route('/query', methods=['GET'])
def get_books():
    topic = request.args.get('topic', type=str)
    if topic is not None:
        return jsonify({'books': [b for b in books if b['topic'] == topic]})
    else:
        id = request.args.get('item', type=int)
        return jsonify({'books': [b for b in books if b['id'] == id]})


@app.route('/update', methods=['PUT'])
def update_books():
    id = request.args.get('item', type=int)
    cost = request.json.get('cost')
    if cost is not None:
        for b in books:
            if b['id'] == id:
                b['cost'] = cost
    else:
        delta = request.json.get('delta')
        for b in books:
            if b['id'] == id:
                b['stock'] += delta  # Add check for zero stock
    return jsonify({'books': [b for b in books if b['id'] == id]})


if __name__ == '__main__':
    df = pd.read_csv('sv_info.txt')
    CATALOG_SERVER = 'http://' + str(df['IP'][0]) + ':' + str(df['Port'][0]) + '/'
    ORDER_SERVER = 'http://' + str(df['IP'][1]) + ':' + str(df['Port'][1]) + '/'
    FRONTEND_SERVER = 'http://' + str(df['IP'][2]) + ':' + str(df['Port'][2]) + '/'

    app.run(host='0.0.0.0', port=df['Port'][0], debug=True)
