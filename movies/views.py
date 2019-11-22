from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse, HttpResponse
from django.contrib.auth import get_user_model

from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

from .serializers import UserSerializer, GenreSerializer, MovieSerializer
from .models import Genre, Movie, Rating, Director
from rest_framework.response import Response



@api_view(['GET'])
@permission_classes([AllowAny, ])
def usersinfo(request):
    users = get_user_model().objects.all()
    serializer = UserSerializer(users, many=True)
    return JsonResponse(serializer.data, safe=False)


@api_view(['GET'])
@permission_classes([AllowAny, ])
def genresinfo(request):
    genres = Genre.objects.all()
    serializer = GenreSerializer(genres, many=True)
    return JsonResponse(serializer.data, safe=False)


@api_view(['GET'])
@permission_classes([AllowAny, ])
def moviesinfo(request):
    movies = Movie.objects.all()
    serializer = MovieSerializer(movies, many=True)
    # return Response(serializer.data)
    return JsonResponse(serializer.data, safe=False)