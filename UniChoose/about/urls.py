from about.views import About
from django.urls import path

app_name = 'aboutpage'

urlpatterns = [
    path('', About.as_view(), name='about'),
]
