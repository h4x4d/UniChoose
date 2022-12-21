import allure

from tests.request_and_check import request


@allure.title('Testing homepage')
def test_homepage_get(client):
    request('/', 200, 'homepage', client)
