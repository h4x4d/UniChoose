from django.urls import path

from universities.views import LikedUniversities

app_name = 'universities'

urlpatterns = [
    path('', LikedUniversities.as_view(), name='liked_unis'),
]
