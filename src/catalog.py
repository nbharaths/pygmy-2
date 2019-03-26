#!flask/bin/python
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
        'stock': 1
    },
    {
        'id': 2,
        'title': book_names['2'],
        'cost': 200,
        'topic': topic_names[0],
        'stock': 1
    },
    {
        'id': 3,
        'title': book_names['3'],
        'cost': 300,
        'topic': topic_names[1],
        'stock': 1
    },
    {
        'id': 4,
        'title': book_names['4'],
        'cost': 400,
        'topic': topic_names[1],
        'stock': 1
    }
]


@app.route('/query', methods=['GET'])
def get_books_by_topic():
    topic = request.args.get('topic', type=str)
    if topic is not None:
        return jsonify({'books': [b for b in books if b['topic'] == topic]})
    else:
        item = request.args.get('item', type=int)
        print(item)
        return jsonify({'books': [b for b in books if b['id'] == item]})


if __name__ == '__main__':
    app.run(debug=True)
