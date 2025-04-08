from django.urls import path
from .views import fitness_chat, chat_page

urlpatterns = [
    path("", chat_page, name="chat_page"),
    path("api/chat/", fitness_chat, name="fitness_chat"),
]