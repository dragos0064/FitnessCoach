from django.urls import path
from .views import fitness_chat

urlpatterns = [
    path("api/chat/", fitness_chat, name="fitness_chat"),
]