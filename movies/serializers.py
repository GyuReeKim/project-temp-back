from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import Genre, Movie, Review, Director, Grade


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = '__all__'




class GradeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Grade
        fields = ('id', 'name',)


class DirectorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Director
        fields = ('id', 'name',)

class MovieSerializer(serializers.ModelSerializer):
    directors = DirectorSerializer(many=True)
    watchgrade = GradeSerializer()
    class Meta:
        model = Movie
        fields = ('id', 'title', 'title_en', 'score', 'audience', 'poster_url', 'summary', 'directors', 'video_url', 'ost_url', 'genres', 'watchgrade',)

class GenreSerializer(serializers.ModelSerializer):
    movies = MovieSerializer(many=True,source='genresmovie')
    # like_users = serializers.SlugRelatedField(many=True, read_only=True, slug_field='username')
    class Meta:
        model = Genre
        fields = ('id', 'name','movies')

class MovieDetailSerializer(serializers.ModelSerializer):
    genres = GenreSerializer(many=True)
    directors = DirectorSerializer(many=True)
    watchgrade = GradeSerializer()
    class Meta:
        model = Movie
        fields = ('id', 'title', 'title_en', 'score', 'audience', 'poster_url', 'summary', 'directors', 'video_url', 'ost_url', 'genres', 'watchgrade',)
        



class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        field = ('id', 'comment', 'score', 'movies', 'users', )