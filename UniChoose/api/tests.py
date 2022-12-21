import allure

from tests.constants import NONEXISTENT_DEPARTMENT
from tests.request_and_check import request
from users.models import AccountDepartmentRelations


@allure.title('Testing preference page with no auth')
def test_preference_get_no_auth(client):
    request('/api/preference/', 403, 'preference', client)


@allure.title('Testing preference page')
def test_preference_get(admin_client):
    request('/api/preference/', 200, 'preference', admin_client)


@allure.title('Testing like page with no auth')
def test_like_get_no_auth(client):
    request('/api/like/111/', 403, 'preference', client)


@allure.title('Testing like page')
def test_like_post(admin_client, admin_user, department, preference):
    relation = AccountDepartmentRelations(department=department,
                                          account=admin_user,
                                          strength=1)
    relation.save()

    request(f'/api/like/{department.id}/', 200, 'like', admin_client, 'post')


@allure.title('Testing like page with no access to department')
def test_like_post_no_access(admin_client, admin_user, department, preference):
    request(f'/api/like/{department.id}/', 403, 'like', admin_client, 'post')


@allure.title('Testing like page with no user preferences')
def test_like_post_no_preference(admin_client, admin_user, department):
    relation = AccountDepartmentRelations(department=department,
                                          account=admin_user,
                                          strength=1)
    relation.save()

    request(f'/api/like/{department.id}/', 403, 'like', admin_client, 'post')


@allure.title('Testing like page with nonexistent department')
def test_like_post_no_department(admin_client, admin_user):
    request(f'/api/like/{NONEXISTENT_DEPARTMENT}/', 404, 'like', admin_client,
            'post')


@allure.title('Testing dislike page')
def test_dislike_post(admin_client, admin_user, department, preference):
    relation = AccountDepartmentRelations(department=department,
                                          account=admin_user,
                                          strength=1)
    relation.save()

    request(f'/api/dislike/{department.id}/', 200, 'dislike', admin_client,
            'post')


@allure.title('Testing dislike page with no user preferences')
def test_dislike_post_no_preference(admin_client, admin_user, department):
    relation = AccountDepartmentRelations(department=department,
                                          account=admin_user,
                                          strength=1)
    relation.save()

    request(f'/api/dislike/{department.id}/', 403, 'dislike', admin_client,
            'post')


@allure.title('Testing dislike page with no access to department')
def test_dislike_post_no_access(admin_client, admin_user, department,
                                preference):
    request(f'/api/dislike/{department.id}/', 403, 'dislike', admin_client,
            'post')


@allure.title('Testing dislike page with nonexistent department')
def test_dislike_post_no_department(admin_client, admin_user):
    request(f'/api/dislike/{NONEXISTENT_DEPARTMENT}/', 404, 'dislike',
            admin_client, 'post')
