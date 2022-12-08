from django.contrib import admin
from django.conf.urls.static import static
from django.urls import path

from UniChoose import settings

urlpatterns = [
    path('admin/', admin.site.urls),
]
