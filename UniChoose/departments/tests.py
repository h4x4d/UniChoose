import allure
import pytest
from hamcrest import assert_that, is_in

from tests.request_and_check import request


@allure.title('Testing liked departments')
def test_departments_get(admin_client):
    request('/departments/', 200, 'departments', admin_client)


@pytest.mark.django_db
@allure.title('Testing liked departments with no authentication')
def test_departments_get_non_authorized(client):
    response = request('/departments/', 302, 'departments', client)

    with allure.step('Asserting redirect link'):
        assert_that(
            '/auth/login/', is_in(response.url),
            f'Expected link was "/auth/login/", '
            f'but got {response.url}')
