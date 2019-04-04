import json
import random

import pytest

import catalog

topic_names = ['ds', 'gs']
book_names = {'1': 'How to get a good grade in 677 in 20 minutes a day',
              '2': 'RPCs for Dummies',
              '3': 'Xen and the Art of Surviving Graduate School',
              '4': 'Cooking for the Impatient Graduate Student'}


@pytest.fixture
def client():
    catalog.app.config['TESTING'] = True
    client = catalog.app.test_client()

    yield client


def test_catalog_query(client):
    """Test that query is logically sound"""
    topic = random.choice(topic_names)
    item_id = random.randint(1, 4)
    base_query = '/query'

    # Testing integrity of topic logic
    response_json = client.get(base_query + '?topic=' + topic).get_json()  # Get JSON response
    assert len(response_json['books']) == 2
    assert response_json['books'][0]['topic'] == topic  # Check if the json has the queried topic
    assert response_json['books'][1]['topic'] == topic

    # Testing integrity of item logic
    response_json = client.get(base_query + '?item=' + str(item_id)).get_json()  # Get JSON response
    assert len(response_json['books']) == 1
    assert response_json['books'][0]['id'] == item_id  # Check if the json has the queried item


def test_catalog_update(client):
    """Test that update is logically sound"""
    topic = random.choice(topic_names)
    item_id = random.randint(1, 4)
    base_update = '/update'
    cost = random.randint(0, 500)
    d = dict(cost=cost)

    # Testing integrity of update logic
    response_json = client.post(base_update + '?item=' + str(item_id), json=d).get_json()  # Get JSON response
    assert len(response_json['books']) == 1
    assert response_json['books'][0]['cost'] == cost  # Check if the json has the correct cost

    delta = random.randint(-10, 10)
    d = dict(delta=delta)
    cat = json.load(open('catalog.json'))
    start_stock = [v['stock'] for v in cat if v['id'] == item_id][0]
    response_json = client.post(base_update + '?item=' + str(item_id), json=d).get_json()  # Get JSON response
    assert len(response_json['books']) == 1
    assert response_json['books'][0]['stock'] == start_stock + delta  # Check if the json has the correct cost
