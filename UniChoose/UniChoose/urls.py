from django.contrib import admin
from django.urls import include, path

from UniChoose import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('django.contrib.auth.urls')),
    # ? path('auth/', include('users.urls')),
    path('', include('homepage.urls')),  # * app_name = 'homepage'
    # * app_name = 'universities'
    path('universities/', include('universities.urls')),
    # * app_name = 'departments'
    path('departments/', include('departments.urls')),
    # * app_name = 'aboutpage'
    path('about/', include('about.urls')),
]

if settings.DEBUG:
    from django.conf.urls.static import static

    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
    urlpatterns += [path('__debug__/', include('debug_toolbar.urls'))]
