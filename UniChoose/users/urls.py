from django.contrib.auth.views import (LoginView, LogoutView,
                                       PasswordChangeDoneView,
                                       PasswordChangeView,
                                       PasswordResetCompleteView,
                                       PasswordResetConfirmView,
                                       PasswordResetDoneView,
                                       PasswordResetView)
from django.urls import path, reverse_lazy
from users.views import EditProfileView, ProfileView, SignUpFormView

app_name = 'auth'

urlpatterns = [
    path('login/', LoginView.as_view(template_name='auth/login.html'),
         name='login'),
    path('logout/', LogoutView.as_view(template_name='auth/logout.html'),
         name='logout'),
    path('password_change/', PasswordChangeView.as_view(
        template_name='users/password_change.html',
        success_url=reverse_lazy('users:password_change_done'),
    ), name='password_change'),

    path('password_change_done/', PasswordChangeDoneView.as_view(
        template_name='users/password_change_done.html',
    ), name='password_change_done'),

    path('password_reset/', PasswordResetView.as_view(
        template_name='users/password_reset.html',
        email_template_name='users/password_reset_email.html',
        success_url=reverse_lazy('users:password_reset_done'),
    ), name='password_reset'),

    path('password_reset_done/', PasswordResetDoneView.as_view(
        template_name='users/password_reset_done.html',
    ), name='password_reset_done'),

    path('password_reset_confirm/<uidb64>/<token>/',
         PasswordResetConfirmView.as_view(
             template_name='users/password_reset_confirm.html',
             success_url=reverse_lazy('users:password_reset_complete'),
         ), name='password_reset_confirm'),

    path('password_reset_complete/', PasswordResetCompleteView.as_view(
        template_name='users/password_reset_complete.html',
    ), name='password_reset_complete'),
    path('signup/', SignUpFormView.as_view(), name='signup'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('profile/edit/', EditProfileView.as_view(), name='profile_edit'),
]
