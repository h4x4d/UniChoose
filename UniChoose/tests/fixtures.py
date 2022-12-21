import allure
import pytest

from departments.models import Department, WeightedDepartment
from universities.models import Region, University
from users.models import Preference


@pytest.mark.django_db
@allure.step('Creating Department')
@pytest.fixture()
def department(db, university):
    department = Department()
    department.name = 'Test department'
    department.edu_level = 0
    department.ege_subjects = ['1', '2', '3']
    department.entry_score = 100
    department.profile = '11.11.11'
    department.university = university

    department.save()

    weighted = WeightedDepartment()
    weighted.department = department
    weighted.profile = 111111
    weighted.edu_level = 0
    weighted.entry_score = 100
    weighted.vuz_rating = 10.0

    weighted.save()

    return department


@pytest.mark.django_db
@allure.step('Creating preference')
@pytest.fixture
def preference(db, admin_user):
    preference = Preference()
    preference.profile = 0
    preference.vuz_rating = 10.0
    preference.entry_score = 310
    preference.edu_level = 0
    preference.user_id = admin_user.id

    preference.save()

    admin_user.preference = preference
    admin_user.save()

    return preference


@pytest.mark.django_db
@allure.step('Creating University')
@pytest.fixture()
def university(db, region):
    university = University()
    university.name = 'Test university'
    university.region = region
    university.avg_rating = 10.0
    university.rating_count = 1000
    university.description = 'Best university!'

    university.save()

    return university


@pytest.mark.django_db
@allure.step('Creating region')
@pytest.fixture()
def region(db):
    region = Region()
    region.name = 'Test region'
    region.latitude = 0
    region.longitude = 0

    region.save()

    return region
