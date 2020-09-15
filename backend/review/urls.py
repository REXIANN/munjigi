from django.urls import path
from .views import ReviewListAPI

urlpatterns = [
    path('', ReviewListAPI.as_view()),
]
