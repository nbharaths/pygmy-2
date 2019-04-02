#!flask/bin/python
import pandas as pd
import requests
from flask import Flask, request

CATALOG_SERVER = 'http://localhost:5000/'

book_names = {'1': 'How to get a good grade in 677 in 20 minutes a day',
              '2': 'RPCs for Dummies',
              '3': 'Xen and the Art of Surviving Graduate School',
              '4': 'Cooking for the Impatient Graduate Student'}

topic_names = ['ds', 'gs']

app = Flask(__name__)


@app.route('/buy', methods=['GET'])
def buy_order():
    id = request.args.get('item', type=int)
    print('Querying for', book_names[str(id)])
    r = requests.get(CATALOG_SERVER + 'query?item=' + str(id))
    print(r.json())
    if r.json()['books'][0]['stock'] > 0:
        b = requests.put(CATALOG_SERVER + 'update?item=' + str(id), json={'delta': -1})
        assert b.status_code == 200
        print('Bought ' + book_names[str(id)])
        return 'Bought ' + book_names[str(id)]
    else:
        print('Out of Stock')
        return 'Out of Stock'


if __name__ == '__main__':
    df = pd.read_csv('sv_info.csv')
    CATALOG_SERVER = 'http://' + str(df['IP'][0]) + ':' + str(df['Port'][0]) + '/'
    ORDER_SERVER = 'http://' + str(df['IP'][1]) + ':' + str(df['Port'][1]) + '/'
    FRONTEND_SERVER = 'http://' + str(df['IP'][2]) + ':' + str(df['Port'][2]) + '/'

    app.run(host='0.0.0.0', port=df['Port'][1], debug=True)
