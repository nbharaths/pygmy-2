import pandas as pd
import requests
from flask import Flask, request

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
    df = pd.read_csv('sv_info.txt')
    CATALOG_SERVER = 'http://' + str(df['IP'][0]) + ':' + str(df['Port'][0]) + '/'
    ORDER_SERVER = 'http://' + str(df['IP'][1]) + ':' + str(df['Port'][1]) + '/'
    FRONTEND_SERVER = 'http://' + str(df['IP'][2]) + ':' + str(df['Port'][2]) + '/'

    app.run(host='0.0.0.0', port=df['Port'][2], debug=True)
