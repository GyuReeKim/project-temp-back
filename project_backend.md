# project_backend

```bash
$ django-admin startproject movieback .
$ django-admin startapp movies
$ django-admin startapp accounts
```





## moviesback

### settings.py

```python
import datetime
```

```python
INSTALLED_APPS = [
    'accounts',
    'movies',
    
    'rest_framework',
    'corsheaders',
```

```python
MIDDLEWARE = [
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',      # 추가
```

```python
LANGUAGE_CODE = 'ko-kr'

TIME_ZONE = 'Asia/Seoul'
```

```python
AUTH_USER_MODEL = 'accounts.User'

REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated',
    ),
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_jwt.authentication.JSONWebTokenAuthentication',
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.BasicAuthentication',
    ),
}

JWT_AUTH ={
    'JWT_SECRET_KEY': SECRET_KEY,
    'JWT_ALGORITHM': 'HS256',
    'JWT_ALLOW_REFRESH': True,
    'JWT_EXPIRATION_DELTA': datetime.timedelta(days=3),
    'JWT_REFRESH_EXPIRATION_DELTA': datetime.timedelta(days=7),
}

CORS_ORIGIN_ALLOW_ALL = True
```



### CORS, JWT설정

```BASH
$ pip install djangorestframework
$ pip install djangorestframework-jwt
$ pip install django-cors-headers
```



### urls.py

```python
from django.contrib import admin
from django.urls import path, include

from rest_framework_jwt.views import obtain_jwt_token

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-token-auth/', obtain_jwt_token),
    path('accounts/', include('accounts.urls')),
    path('api/v1/', include('movies.urls')),
]
```







## movies

### models.py

```python
from django.db import models
from django.contrib.auth import settings


class Genre(models.Model):
    typename = models.CharField(max_length=150)
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_genres')
    # 장르 좋아요(장르 추천)

class Movie(models.Model):
    title = models.CharField(max_length=150)
    summary = models.TextField()
    director = models.CharField(max_length=45)
    genre = models.ManyToManyField(Genre, related_name='')

    title_en = models.CharField(max_length=150)
    score = models.IntegerField()
    poster_url = models.CharField(max_length=500)
    video_url = models.CharField(max_length=500, null=True)
    ost_url = models.CharField(max_length=500, null=True)
    # like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="like_movies")
    # 영화 좋아요

class Rating(models.Model):
    comment = models.TextField()
    score = models.IntegerField()
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
```



### serializers.py

```python
from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import Genre, Director, Actor, Movie, Hashtag, Post


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = '__all__'


class GenreSerializer(serializers.ModelSerializer):
    like_users = serializers.SlugRelatedField(many=True, read_only=True, slug_field='username')
    class Meta:
        model = Genre
        fields = ('like_users',)


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ('id', 'title', 'title_en', 'score', 'poster_url', 'summary', 
        'director', 'poster_url', 'video_url', 'ost_url', 'genre',)
        
```

`SlugRelatedField` 대상의 필드를 사용하여 관계의 대상을 나타내는 데 사용될 수 있습니다.

```python
class AlbumSerializer(serializers.ModelSerializer):
    tracks = serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field='title'
     )

    class Meta:
        model = Album
        fields = ['album_name', 'artist', 'tracks']
```

```
{
    'album_name': 'Dear John',
    'artist': 'Loney Dear',
    'tracks': [
        'Airport Surroundings',
        'Everything Turns to You',
        'I Was Only Going Out',
        ...
    ]
}
```

`read_only`플래그를 사용하여이 동작을 변경할 수 있지만 기본적으로이 필드는 읽기 / 쓰기 입니다.

사용하는 경우 `SlugRelatedField`읽기 - 쓰기 필드로, 당신은 일반적으로 모델 필드에 그 슬러그 필드와 일치하는지 확인하는 것이 좋습니다 `unique=True`.

**인수** :

- `slug_field`-대상을 나타내는 데 사용해야하는 필드입니다. 주어진 인스턴스를 고유하게 식별하는 필드 여야합니다. 예를 들면 다음과 같습니다 `username`. **필수**
- `queryset`-필드 입력의 유효성을 검사 할 때 모델 인스턴스 조회에 사용되는 쿼리 집합입니다. 관계는 명시 적으로 queryset을 설정하거나을 설정해야합니다 `read_only=True`.
- `many`-다 대다 관계에 적용되는 경우이 인수를로 설정해야합니다 `True`.
- `allow_null`-로 설정된 경우 `True`필드는 `None`nullable 관계에 대한 값 또는 빈 문자열을 허용합니다. 기본값은 `False`입니다.







## accounts

### models.py

```python
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
```



### serializers.py

```python
from rest_framework import serializers
from .models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email', 'password', 'genre_liker',)
```

