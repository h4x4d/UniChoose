import allure

from tests.request_and_check import request


@allure.title('Testing about page')
def test_about_get(client):
    request('/about/', 200, 'about', client)
