from django.core import serializers
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from trips_be.apps.auth.serializers import UserSerializer, TourGuideSerializer

@csrf_exempt
@api_view(["POST"])
@permission_classes((AllowAny,))
def signup(request):

    username = request.data.get("username")
    password = request.data.get("password")
    user_mail = request.data.get('email')

    try:
        user = User.objects.get(username=username)
    except User.DoesNotExist:
        user = None

    if user:
        return Response({'error': 'user already exits'}, status=status.HTTP_400_BAD_REQUEST)
    else:
        User.objects.create_user(username, user_mail, password)
        return Response(status=status.HTTP_200_OK)

@csrf_exempt
@api_view(["GET"])
def get_user(request):

    username = request.query_params.get('username', None)
    
    if username:
        user_query = User.objects.get(username=username)
        if user_query:
            user = UserSerializer(instance=user_query).data
            return Response(user, status=status.HTTP_200_OK)
        else:
            return Response({'error':'username doesn\'t exists'},status=status.HTTP_400_BAD_REQUEST)
    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)

@csrf_exempt
@api_view(["POST"])
def fill_tour_guide_data(request):
    guide_data_serialized = TourGuideSerializer(data=request.data)
    if guide_data_serialized.is_valid():
        guide_data_serialized.save()
        return Response(status=status.HTTP_200_OK)
    print(guide_data_serialized.errors)
    print(request.data)
    return Response(guide_data_serialized.errors, status=status.HTTP_400_BAD_REQUEST)