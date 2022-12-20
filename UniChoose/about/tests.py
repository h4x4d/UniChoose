import allure
from hamcrest import assert_that, equal_to


@allure.title('Testing about page')
def test_about_get(client):
    with allure.step('Getting about page'):
        response = client.get('/')
    with allure.step('Asserting status'):
        assert_that(response.status_code, equal_to(200),
                    f'Expected code was 200, but got {response.status_code}')
