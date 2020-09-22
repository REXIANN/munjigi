from django.urls import path
from . import views
from .views import HeritageListAPI, HeritageDetailAPI, HeritageLikeAPI

urlpatterns = [
    path('', HeritageListAPI.as_view()),
    path('<int:pk>/', HeritageDetailAPI.as_view()),
    path('<int:pk>/like/', HeritageLikeAPI.as_view()),
]
