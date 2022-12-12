import os
import threading

os.chdir('..')


def f(i):
    os.system(f'python manage.py loaddata '  # noqa
              f'fixtures/initial_fixtures/data_fixture_{i}.json')


for i in range(1, 455):
    th = threading.Thread(target=f, args=[i])
    th.start()
