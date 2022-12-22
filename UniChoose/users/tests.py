import allure
from hamcrest import assert_that, is_in

from tests.request_and_check import request


@allure.title('Testing login page')
def test_login_get(client):
    request('/auth/login/', 200, 'login', client)


@allure.title('Testing logout page')
def test_logout_get(client):
    request('/auth/logout/', 200, 'logout', client)


@allure.title('Testing password change page with no login')
def test_password_change_get(client):
    response = request('/auth/password_change/', 302, 'password_change',
                       client)

    with allure.step('Asserting redirect link'):
        assert_that(
            '/auth/login/', is_in(response.url),
            f'Expected link was "/auth/login/", '
            f'but got {response.url}')
