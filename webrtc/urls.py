from django.urls import path
from .views import *

app_name = 'webrtc'

urlpatterns = [
    path('<str:name>/', RoomView.as_view(), name='room'),
]
