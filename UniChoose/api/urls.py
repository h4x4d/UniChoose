from django.urls import include, path
from rest_framework import routers

from api.views import APIDislike, APILike, DepartmentViewSet, PreferenceViewSet

router = routers.DefaultRouter()
router.register(r'departments', DepartmentViewSet)
router.register(r'preference', PreferenceViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path(r'like/<int:pk>/', APILike.as_view()),
    path(r'dislike/<int:pk>/', APIDislike.as_view()),
    path('api-auth/', include('rest_framework.urls',
                              namespace='rest_framework')),
]
