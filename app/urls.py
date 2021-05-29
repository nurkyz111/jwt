from django.urls import path
from .views import App

app_name = 'app'

urlpatterns = [
    path('', App.as_view(), name='app'),
]