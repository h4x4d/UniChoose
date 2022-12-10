from django.contrib import admin
from django.urls import path, include

from UniChoose import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('django.contrib.auth.urls')),
    # path('auth/', include('users.urls')),
    path('', include('homepage.urls')),     # app_name = 'homepage'
    # app_name = 'universities'
    path('universities/', include('universities.urls')),
    # app_name = 'departments'
    path('departments/', include('departments.urls')),
    path('about/', include('about.urls')),  # app_name = 'aboutpage'
]

if settings.DEBUG:
    from django.conf.urls.static import static

    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
