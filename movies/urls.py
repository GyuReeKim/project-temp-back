from django.urls import path
from . import views

urlpatterns = [
    path('users/', views.users),
    path('genres/', views.genres),
    path('grades/', views.grades),
    path('directors/', views.directors),
    path('movies/', views.movies),
    path('review/', views.review),

    path('<int:movie_id>/', views.movies_detail),
    path('<int:movie_id>/reviews/', views.create_reviews),
    path('reviews/<int:review_id>/', views.reviews_detail)
]