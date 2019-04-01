import requests
from flask import Flask, request

CATALOG_SERVER = 'http://localhost:5000/'
ORDER_SERVER = 'http://localhost:5001/'
FRONTEND_SERVER = 'http://localhost:5002/'

actions = ['search', 'lookup', 'buy']
topics = ['ds', 'gs']
app = Flask(__name__)


@app.route('/search', methods=['GET'])
def search():
    topic = request.args.get('topic', type=str)
    if topic is not None:
        r = requests.get(CATALOG_SERVER + 'query?topic=' + topic)
        return r.text


@app.route('/lookup', methods=['GET'])
def lookup():
    item_number = request.args.get('item', type=int)
    r = requests.get(CATALOG_SERVER + 'query?item=' + str(item_number))
    return r.text


@app.route('/buy', methods=['GET'])
def buy():
    item_number = request.args.get('item', type=int)
    r = requests.get(ORDER_SERVER + 'buy?item=' + str(item_number))
    return r.text


if __name__ == '__main__':
    app.run(debug=True, port=5002)
