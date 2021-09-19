from rest_framework import generics
from message.models import Message
from message.api.serializers import MessageSerializer
from message.api.pagination import SmallSetPagination
from message.api.permissions import IsMessageSenderOrReceiver

class MessageListCreateAPIView(generics.ListCreateAPIView):
    serializer_class = MessageSerializer
    pagination_class = SmallSetPagination
    permission_classes = [IsMessageSenderOrReceiver]

    def get_queryset(self):
        user = self.request.user
        return Message.objects.filter(sender=user).order_by("id") | Message.objects.filter(receiver=user).order_by("id")

    def perform_create(self, serializer):
        sender = self.request.user
        serializer.save(sender=sender)

class MessageDetailAPIView(generics.RetrieveDestroyAPIView):
    serializer_class = MessageSerializer
    permission_classes = [IsMessageSenderOrReceiver]

    def get_queryset(self):
        user = self.request.user
        messages = Message.objects.filter(receiver=user, is_read=False).first()
        if messages:
            messages.is_read = True
            messages.save()
        return Message.objects.filter(receiver=user) | Message.objects.filter(sender=user)