from django.urls import path

from trips_be.apps.auth.views import signup, get_user, fill_tour_guide_data

urlpatterns = [
    path('signup', signup),
    path('user', get_user),
    path('tour_guide', fill_tour_guide_data)
]