from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.timezone import now
from datetime import timedelta


# Create your models here.

class User(AbstractUser):
    avatar = models.ImageField(upload_to='users_avatars', blank=True)
    activation_key = models.CharField(max_length=128, blank=True)
    activation_key_expiring = models.DateTimeField(default=(now() + timedelta(hours=48)))

    def activation_key_expired(self):
        return now() >= self.activation_key_expiring
