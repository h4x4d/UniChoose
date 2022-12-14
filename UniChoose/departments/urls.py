from departments.views import LikedDepartments
from django.urls import path

app_name = 'departments'

urlpatterns = [
    path('', LikedDepartments.as_view(), name='liked_dpts'),
]
