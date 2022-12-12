import json
import os

import requests

url = 'https://geocode-maps.yandex.ru/1.x'
key = os.environ.get('geocoder_key')

addresses = {
    i['region']
    for i in json.load(open('data.json', encoding='utf-8'))
}

addresses_with_coords = {}
fixture = []

for address in addresses:
    response = requests.get(url,
                            params={
                                'geocode': address,
                                'apikey': key,
                                'format': 'json',
                            })
    r = response.json()
    pos = r['response']['GeoObjectCollection']['featureMember'][0][
        'GeoObject']['Point']['pos']
    lat, lon = pos.split()

    addresses_with_coords[address] = (float(lat), float(lon))

for j, i in enumerate(addresses_with_coords.keys()):
    fixture.append({
        'pk': j + 1,
        'model': 'universities.Region',
        'fields': {
            'name': i,
            'latitude': addresses_with_coords[i][0],
            'longitude': addresses_with_coords[i][1],
        },
    })

json.dump(fixture,
          open('address_fixture.json', 'w', encoding='utf-8'),
          ensure_ascii=False,
          indent=4)
