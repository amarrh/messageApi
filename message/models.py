from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username

class Message(models.Model):
    
    H = 'H'
    M = 'M'
    L = 'L'
    IMPORTANCE_CHOICES = [
        (H, 'H'),
        (M, 'M'),
        (L, 'L'),
    ]
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sender')
    receiver = models.ForeignKey(User, on_delete=models.CASCADE, related_name='receiver')
    summary = models.CharField(max_length=25)
    message = models.CharField(max_length=250)
    importance = models.CharField(
        max_length=1,
        choices=IMPORTANCE_CHOICES,
        default=L,
    )
    is_read = models.BooleanField(default=False)

    def __str__(self):
        return f"{ self.summary } { self.message }"