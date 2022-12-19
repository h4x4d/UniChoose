import json

with open('address_fixture.json', 'r', encoding='utf-8') as file:
    addresses = json.load(file)

    stripped = []
    for addr in addresses:
        stripped.append(addr['fields']['name'])

    stripped = sorted(stripped)

    py_file = open('region_choice_field_fixture.py', 'w', encoding='utf-8')
    py_file.write('region_choices = ' +
                  json.dumps(stripped, ensure_ascii=False))
    py_file.close()
