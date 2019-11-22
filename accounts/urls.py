from django.urls import path
from . import views

urlpatterns = [
    path('userfind/', views.userfind),
    # path('signup/', views.signup),
    # path('login/', views.login),
    # path('logout/', views.logout),
    
]