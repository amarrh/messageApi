from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework.relations import StringRelatedField
from message.models import Message


class MessageSerializer(serializers.ModelSerializer):
    sender = StringRelatedField(read_only=True)
    receiver = serializers.SlugRelatedField(many=False, slug_field='username', queryset=User.objects.all())
    is_read = serializers.BooleanField(default=False, read_only=True)

    class Meta:
        model = Message
        fields = ['id', 'sender', 'receiver', 'summary', 'message', 'importance', 'is_read']
