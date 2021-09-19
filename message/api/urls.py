from django.urls import path
from message.api.views import MessageListCreateAPIView, MessageDetailAPIView

urlpatterns = [
    path("messages/", MessageListCreateAPIView.as_view(), name="message-list"),
    path("messages/<int:pk>", MessageDetailAPIView.as_view(), name="message-detail"),
]