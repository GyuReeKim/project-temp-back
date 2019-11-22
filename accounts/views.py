from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse, HttpResponse
from django.contrib.auth.forms import AuthenticationForm

from rest_framework.decorators import api_view, permission_classes
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny

from django.contrib.auth import get_user_model
from .models import User
from .serializers import UserSerializer
from .forms import CreateUserForm

# from django.contrib.auth import login as auth_login
# from django.contrib.auth import logout as auth_logout
# from django.contrib.auth.decorators import login_required


@api_view(['GET'])
@permission_classes([AllowAny, ])
def userfind(request):
    users = get_user_model().objects.all()
    serializer = UserSerializer(users, many=True)
    return JsonResponse(serializer.data, safe=False)


# def signup(request):
#     if request.method == 'POST':
#         form = CreateUserForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('accounts:login')
#     else:
#         form = CreateUserForm()
#     context = {
#         'form':form
#     }
#     return render(request, 'accounts/form.html', context)


# def login(request):
#     if request.method == 'POST':
#         form = AuthenticationForm(request, request.POST)
#         if form.is_valid():
#             auth_login(request, form.get_user())
#             return redirect('movies:index')
#     else:
#         form = AuthenticationForm()
#     context = {
#         'form':form
#     }
#     return render(request, 'accounts/form.html', context)


# @login_required
# def logout(request):
#     if request.method == 'POST':
#         auth_logout(request)
#     return redirect('movies:index')