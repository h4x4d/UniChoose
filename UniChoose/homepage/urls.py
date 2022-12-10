from django.urls import path
from homepage.views import home

app_name = 'homepage'
urlpatterns = [
    path('', home, name='home'),
]
