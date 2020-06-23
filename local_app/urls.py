from django.urls import path
from . import views
import requests
import json
from .config import get_my_key


urlpatterns = [
    path('', views.home, name="home"),
    path('<slug:id>/', views.location_details, name="location_details"),
    path('savepins/', views.save_pins, name="save_pins"),
    path('addtrip/<slug:id>/', views.add_trip, name="add_trip"),
    path('mypins/',views.my_pins, name="my_pins" ),
]