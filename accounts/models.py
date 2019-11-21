from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
from movies.models import Genre

# Create your models here.

class User(AbstractUser):
    genre_liker = models.ManyToManyField(Genre, related_name='liker_users')
    # accounts_user_genre_liker
    followers = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="followings")
    # 팔로워 팔로잉 기능