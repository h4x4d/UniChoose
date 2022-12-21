import allure
from hamcrest import assert_that, equal_to


def request(page, status_code, page_name, client, type_of_request='get'):
    if type_of_request == 'get':
        with allure.step(f'Getting {page_name} page'):
            response = client.get(page)
    elif type_of_request == 'post':
        with allure.step(f'Getting {page_name} page'):
            response = client.get(page)
    else:
        raise Exception(f'Unsupported type of requst {type_of_request}')

    with allure.step('Asserting status'):
        assert_that(
            response.status_code, equal_to(status_code),
            f'Expected code was {status_code}, '
            f'but got {response.status_code}')

    return response
