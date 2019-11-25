from rest_framework import serializers
from .models import Genre, Movie, Review, Director, Grade


class GradeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Grade
        fields = ('id', 'name',)

class DirectorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Director
        fields = ('id', 'name',)

class MovieSerializer(serializers.ModelSerializer):
    # movie_genres = GenreSerializer(many=True)
    movie_directors = DirectorSerializer(many=True)
    grade = GradeSerializer()
    class Meta:
        model = Movie
        fields = ('id', 'title', 'title_en', 'score', 'audience', 'poster_url', 
        'summary', 'movie_directors', 'video_url', 'ost_url', 'movie_genres', 'grade',)

class GenreSerializer(serializers.ModelSerializer):
    movies = MovieSerializer(many=True, source='genre_movies')
    # like_users = serializers.SlugRelatedField(many=True, read_only=True, slug_field='username')
    class Meta:
        model = Genre
        fields = ('id', 'name', 'movies')

class MovieDetailSerializer(serializers.ModelSerializer):
    movie_genres = GenreSerializer(many=True)
    movie_directors = DirectorSerializer(many=True)
    grade = GradeSerializer()
    class Meta:
        model = Movie
        fields = ('id', 'title', 'title_en', 'score', 'audience', 'poster_url',
         'summary', 'movie_directors', 'video_url', 'ost_url', 'movie_genres', 'grade',)


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        field = ('id', 'comment', 'score', 'movie', 'review_user', )