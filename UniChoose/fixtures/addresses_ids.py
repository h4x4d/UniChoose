import json


def get_address_ids():
    f = open('address_fixture.json', encoding='utf-8')
    data = {}

    for i in json.load(f):
        data[i['fields']['name']] = i['pk']

    return data
