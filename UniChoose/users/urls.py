from django.contrib.auth.views import (LoginView, LogoutView,
                                       PasswordChangeDoneView,
                                       PasswordChangeView)
from django.urls import path, reverse_lazy

from users.views import (EditProfileView, ProfileView, SelectSubjectsView,
                         SignUpFormView)

app_name = 'auth'

urlpatterns = [
    path('login/',
         LoginView.as_view(template_name='auth/login.html',
                           success_url=reverse_lazy('homepage:home')),
         name='login'),
    path('logout/',
         LogoutView.as_view(template_name='auth/logout.html'),
         name='logout'),
    path('password_change/',
         PasswordChangeView.as_view(
             template_name='auth/password_change.html',
             success_url=reverse_lazy('auth:password_change_done'),
         ),
         name='password_change'),
    path('password_change/done/',
         PasswordChangeDoneView.as_view(
             template_name='auth/password_change_done.html'),
         name='password_change_done'),
    path('signup/', SignUpFormView.as_view(), name='signup'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('profile/edit/', EditProfileView.as_view(), name='profile_edit'),
    path('edit_info/', SelectSubjectsView.as_view(), name='edit_info'),
]
