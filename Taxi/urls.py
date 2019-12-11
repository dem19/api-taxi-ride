from django.urls import path
from django.urls import path
from Taxi.views import CustomAuthToken


urlpatterns = [

    path('token/', CustomAuthToken.as_view())
]