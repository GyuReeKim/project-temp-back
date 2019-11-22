from django.urls import path
from . import views

urlpatterns = [
    path('usersinfo/', views.usersinfo),
    path('genresinfo/', views.genresinfo),
    path('moviesinfo/', views.moviesinfo),
]