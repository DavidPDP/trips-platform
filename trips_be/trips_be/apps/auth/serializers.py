from django.contrib.auth.models import User
from rest_framework import serializers

from trips_be.apps.auth.models import TourGuide

class TourGuideSerializer(serializers.ModelSerializer):
    class Meta:
        model = TourGuide
        fields = ['user', 'description', 'identification', 'email', 'address', 'telephone']

class UserSerializer(serializers.ModelSerializer):

    tourguide_id = serializers.IntegerField(write_only=True)
    tourguide = TourGuideSerializer(read_only=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'tourguide_id', 'tourguide']