from rest_framework import generics
from .models import App
from .serializers import AppSerializer


class App(generics.ListAPIView):

    serializer_class = AppSerializer
    queryset = App.objects.all()

