from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import Genre, Movie, Rating


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = '__all__'


class GenreSerializer(serializers.ModelSerializer):
    like_users = serializers.SlugRelatedField(many=True, read_only=True, slug_field='username')
    class Meta:
        model = Genre
        fields = ('id', 'typename', 'like_users',)


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ('id', 'title', 'title_en', 'score', 'audience', 'poster_url', 'summary', 'director', 'poster_url', 'video_url', 'ost_url', 'genre',)
        