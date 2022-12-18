import json
from operator import itemgetter

with open('address_fixture.json', 'r', encoding='utf-8') as file:
    addresses = json.load(file)

    stripped = [('0', 'Выберите ваш регион...')]
    for addr in addresses:
        stripped.append((str(addr['pk']), addr['fields']['name']))

    stripped = sorted(stripped, key=itemgetter(1))

    py_file = open('region_choice_field_fixture.py', 'w', encoding='utf-8')
    py_file.write('region_choices = ' +
                  json.dumps(stripped, ensure_ascii=False))
    py_file.close()
