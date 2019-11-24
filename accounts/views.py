from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse, HttpResponse
from django.contrib.auth.forms import AuthenticationForm

from rest_framework.decorators import api_view, permission_classes

from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework_jwt.settings import api_settings

from django.contrib.auth import get_user_model
from .models import User
from .serializers import UserSerializer
from .forms import CreateUserForm


@api_view(['GET'])
@permission_classes([IsAuthenticated, ])
def userfind(request):
    users = get_user_model().objects.all()
    serializer = UserSerializer(users, many=True)
    return JsonResponse(serializer.data, safe=False)



@api_view(['POST'])
@permission_classes([IsAuthenticated, ])
def signup(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
        jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER
        user = serializer.save()

        payload = jwt_payload_handler(user)
        token = jwt_encode_handler(payload)

        return JsonResponse({'token': token})
    return HttpResponse(status=400)