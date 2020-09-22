from django.urls import path
from .views import RegistrationAPI, LoginAPI, UserAPI, ProfileAPI, RegistrationCheckAPI

urlpatterns = [
    path('auth/register/', RegistrationAPI.as_view()),
    path('auth/login/', LoginAPI.as_view()),
    path('auth/user/', UserAPI.as_view()),
    path('<nickname>/', ProfileAPI.as_view()),
    path('register/<checking>/', RegistrationCheckAPI.as_view()),
]
