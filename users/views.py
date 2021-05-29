from django.contrib.auth import get_user_model

from rest_framework import generics
from users.serializers import UserRegisterSerializer


class UserRegisterAPIView(generics.CreateAPIView):
    model = get_user_model()
    serializer_class = UserRegisterSerializer
