#!flask/bin/python
import requests
from flask import Flask, request

CATALOG_SERVER = 'http://localhost:5000/'
ORDER_SERVER = 'http://localhost:5001/'
FRONTEND_SERVER = 'http://localhost:5002/'

book_names = {'1': 'How to get a good grade in 677 in 20 minutes a day',
              '2': 'RPCs for Dummies',
              '3': 'Xen and the Art of Surviving Graduate School',
              '4': 'Cooking for the Impatient Graduate Student'}

topic_names = ['ds', 'gs']

app = Flask(__name__)


@app.route('/buy', methods=['GET'])
def buy_order():
    id = request.args.get('item', type=int)
    r = requests.get(CATALOG_SERVER + 'query?item=' + str(id))
    print(r.json())
    if r.json()['books'][0]['stock'] > 0:
        b = requests.put(CATALOG_SERVER + 'update?item=' + str(id), json={'delta': -1})
        return 'Bought ' + book_names[str(id)]
    else:
        return 'Out of Stock'


if __name__ == '__main__':
    app.run(debug=True, port=5001)
