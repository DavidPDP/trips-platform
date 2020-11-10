from datetime import datetime

from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from trips_be.apps.trips.serializers import TripSerializer, BookingSerializer, LikeSerializer
from trips_be.apps.auth.serializers import UserSerializer, TourGuideSerializer
from trips_be.apps.trips.models import Trip, Booking, Like

@csrf_exempt
@api_view(["POST"])
def create_trip(request):
    trip_serialized = TripSerializer(data=request.data)
    if trip_serialized.is_valid():
        trip_serialized.save()
        return Response(status=status.HTTP_200_OK)
    print(trip_serialized.errors)
    return Response(trip_serialized.errors, status=status.HTTP_400_BAD_REQUEST)

@csrf_exempt
@api_view(["GET"])
def list_trips(request):
    last_trip = request.query_params.get('last_trip', None)
    if last_trip:
        # limit executes in db.
        trips_query = Trip.objects.filter(id__gt = int(last_trip))[:10]
        print(trips_query)
        trips = TripSerializer(trips_query, many=True).data
        return Response(trips, status=status.HTTP_200_OK)
    return Response(status=status.HTTP_400_BAD_REQUEST)

@csrf_exempt
@api_view(["POST"])
def create_booking(request):
    booking_serialized = BookingSerializer(data=request.data)
    if booking_serialized.is_valid():
        booking_serialized.save()
        return Response(status=status.HTTP_200_OK)
    return Response(booking_serialized.errors, status=status.HTTP_400_BAD_REQUEST)

@csrf_exempt
@api_view(["GET"])
def list_bookings(request):
    # limit executes in db.
    bookings_query = Booking.objects.all()
    bookings = BookingSerializer(bookings_query, many=True).data
    return Response(bookings, status=status.HTTP_200_OK)

@csrf_exempt
@api_view(["POST"])
def increment_likes(request):
    trip_id = request.data['trip_id']
    if(trip_id):
        trip_query = Trip.objects.get(id=trip_id)
        if trip_query:
            trip_query.likes = trip_query.likes + 1
            trip_query.save()
            return Response(status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)

@csrf_exempt
@api_view(["POST"])
def decrement_likes(request):
    trip_id = request.data['trip_id']
    if(trip_id):
        trip_query = Trip.objects.get(id=trip_id)
        if trip_query:
            trip_query.likes = trip_query.likes - 1
            trip_query.save()
            return Response(status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)
