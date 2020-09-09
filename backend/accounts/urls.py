from django.ruls import path, include
from .api import RegisterAPI
from knox import views as knox_views
 
urlpatterns = [
    path('auth/register', RegisterAPI.as_view())
]
