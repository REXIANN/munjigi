from django.urls import path
from .views import HeritageListAPI

urlpatterns = [
    path('', HeritageListAPI.as_view()),
]
