from django.urls import path

from trips_be.apps.trips.views import (create_trip, list_trips, create_booking, 
    list_bookings, increment_likes, decrement_likes)

urlpatterns = [
    path('', create_trip),
    path('list', list_trips),
    path('booking', create_booking),
    path('booking/list', list_bookings),
    path('likes/increment', increment_likes),
    path('likes/decrement', decrement_likes)
]