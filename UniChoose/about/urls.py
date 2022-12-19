from django.urls import path

from about.views import About

app_name = 'aboutpage'

urlpatterns = [
    path('', About.as_view(), name='about'),
]
