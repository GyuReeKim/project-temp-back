from django.db import models
from django.contrib.auth import settings


class Genre(models.Model):
    typename = models.CharField(max_length=150)
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_genres')
    # 장르 좋아요(장르 추천)
    def __str__(self):
        return "{}. {}".format(self.id, self.typename)


class Director(models.Model):
    director = models.CharField(max_length=45)
    def __str__(self):
        return "{}. {}".format(self.id, self.director)


class Movie(models.Model):
    title = models.CharField(max_length=150)
    summary = models.TextField()
    director =  models.ManyToManyField(Director, related_name='directormovie')
    genre = models.ManyToManyField(Genre, related_name='genremovie')

    title_en = models.CharField(max_length=150)
    score = models.FloatField()
    audience = models.IntegerField()
    poster_url = models.CharField(max_length=500)
    video_url = models.CharField(max_length=500, null=True)
    ost_url = models.CharField(max_length=500, null=True)
    # like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="like_movies")
    # 영화 좋아요
    def __str__(self):
        return "{}. {}".format(self.id, self.title)

class Rating(models.Model):
    comment = models.TextField()
    score = models.FloatField()
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)