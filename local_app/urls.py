from django.urls import path
from . import views
import requests
import json
from .config import get_my_key

app_name = "local_app" 

urlpatterns = [
    path('', views.home, name="home"),
    path('<slug:id>/', views.location_details, name="location_details"),
    path('savepins/<slug:id>', views.save_pins, name="save_pins"),
    path('addtrip/<int:id>', views.add_trip, name="add_trip"),
    path('mypins',views.my_pins, name="my_pins" ),
    path('mytrips', views.my_trips, name="my_trips"),
    path('removepins/<int:id>', views.remove_pins, name="remove_pins"),
    path('removetrip/<int:id>', views.remove_trip, name="remove_trip"),
    path('deleteall', views.delete_all, name="delete_all"),
]