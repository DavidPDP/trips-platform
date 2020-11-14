from django.urls import path, include
from rest_framework_simplejwt.views import (TokenObtainPairView, TokenRefreshView)

urlpatterns = [
    path('auth/', include(('trips_be.apps.auth.urls', 'auth'))),
    path('auth/signin', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('auth/refresh', TokenRefreshView.as_view(), name='token_refresh'),
    path('trips/', include(('trips_be.apps.trips.urls', 'trips')))
]