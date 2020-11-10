from rest_framework import serializers

from trips_be.apps.trips.models import Trip, Booking, Like
from trips_be.apps.auth.serializers import UserSerializer, TourGuideSerializer

class TripSerializer(serializers.ModelSerializer):
    
    user_id = serializers.IntegerField(write_only=True)
    user = UserSerializer(read_only=True)

    class Meta:
        model = Trip
        fields = ('id', 'user_id', 'user', 'description', 'price', 'match', 
            'long_days', 'location', 'date', 'likes')

class BookingSerializer(serializers.ModelSerializer):

    trip_id = serializers.IntegerField(write_only=True)
    trip = TripSerializer(read_only=True)

    class Meta:
        model = Booking
        fields = ['trip_id', 'trip', 'user']

class LikeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Like
        fields = ['trip', 'user', 'amount']