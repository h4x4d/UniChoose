import allure
import pytest
from hamcrest import assert_that, equal_to, is_in


@allure.title('Testing liked departments')
def test_departments_get(admin_client):

    with allure.step('Getting liked departments'):
        response = admin_client.get('/departments/')
    with allure.step('Asserting status'):
        assert_that(response.status_code, equal_to(200),
                    f'Expected code was 200, but got {response.status_code}')


@pytest.mark.django_db
@allure.title('Testing liked departments with no authentication')
def test_departments_get_non_authorized(client):
    with allure.step('Getting liked departments'):
        response = client.get('/departments/')
    with allure.step('Asserting status'):
        assert_that(response.status_code, equal_to(302),
                    f'Expected code was 302, but got {response.status_code}')

    with allure.step('Asserting redirect link'):
        assert_that(
            '/auth/login/', is_in(response.url),
            f'Expected link was "/auth/login/", '
            f'but got {response.url}')
