from django.urls import path
from departments.views import LikedDepartments

app_name = 'departments'

urlpatterns = [
    path('', LikedDepartments.as_view(), name='liked_dpts'),
]
