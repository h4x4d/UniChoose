import json

from fixtures.addresses_ids import get_address_ids

levels_int = {
    'Бакалавриат': 0,
    'Специалитет': 1,
    'Магистратура': 2,
}

regions = get_address_ids()


def main(source_file, fixture_file):
    data = json.load(open(source_file, encoding='utf-8'))
    fixture = []
    university_pk = 1
    department_pk = 1

    for university in data:
        if university['rating'][1] == 'Нет оценок':
            university['rating'][1] = 0

        fixture.append({
            'pk': university_pk,
            'model': 'universities.university',
            'fields': {
                'name': university['name'],
                'description': university['description'],
                'avg_rating': university['rating'][0],
                'rating_count': university['rating'][1],
                'region': regions[university['region']],
            },
        })

        for profile in university['napravlenie']:
            for department in profile['podrazdelenie']:
                if department['pass_mark'] == 'Нет' or \
                   department['pass_mark'] == 'БВИ':
                    department['pass_mark'] = 0

                for j, i in enumerate(department['ege_subjects']):
                    if 'или' in i:
                        department['ege_subjects'][j] = i.split('  или ')
                    try:
                        department['ege_subjects'].remove('Внутренний экзамен')
                    except ValueError:
                        pass

                fixture.append({
                    'pk': department_pk,
                    'model': 'departments.department',
                    'fields': {
                        'name': department['name'],
                        'profile': department['profile'],
                        'profile_class': department['number'],
                        'entry_score': department['pass_mark'],
                        'edu_level': levels_int[profile['level']],
                        'ege_subjects': department['ege_subjects'],
                        'university': university_pk,
                    },
                })
                department_pk += 1
        """json.dump(fixture,
                  open(
                      f'initial_fixtures/{fixture_file}_'
                      f'{university_pk}.json',
                      'w',
                      encoding='utf-8'),
                  ensure_ascii=False,
                  indent=4)
        fixture = []"""

        university_pk += 1

    json.dump(fixture,
              open('fixture.json', 'w', encoding='utf-8'),
              ensure_ascii=False,
              indent=4)
    fixture = []


if __name__ == '__main__':
    main('data.json', 'data_fixture')
