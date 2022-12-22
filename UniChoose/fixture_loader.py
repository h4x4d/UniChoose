import django
from django.core.management import call_command
from django.db import transaction

django.setup()

with transaction.atomic():
    call_command('loaddata', 'fixtures/fixture.json')
