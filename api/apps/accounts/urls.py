from django.urls import path, include

from .views import (
    AccountCreateAPIView,
    LoginAPIView,
    RegistrationAPIView,
    UserRetrieveUpdateAPIView,
    ActivateUserAccount,
    PasswordResetView,
)


urlpatterns = [
    path(
        "accounts/",
        AccountCreateAPIView.as_view()),
    path(
        "user/",
        UserRetrieveUpdateAPIView.as_view()),
    path(
        "users/",
        RegistrationAPIView.as_view()),
    path(
        "users/login/",
        LoginAPIView.as_view()),
    path(
        "users/activate/<uidb64>/<token>/",
        ActivateUserAccount.as_view(),
        name="activate_user_account",
    ),
    path(
        'password_reset/',
        include(
            'django_rest_passwordreset.urls',
            namespace='password_reset')),
    path(
        "reset-password/<token>",
        PasswordResetView.as_view(),
        name="password_reset_verify_token",
    ),
]
