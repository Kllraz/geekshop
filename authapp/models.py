from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.timezone import now
from datetime import timedelta

from django.dispatch import receiver
from django.db.models.signals import post_save


# Create your models here.

class User(AbstractUser):
    avatar = models.ImageField(upload_to='users_avatars', blank=True)
    birthday = models.DateField(verbose_name='дата рождения', default=now, blank=True)
    activation_key = models.CharField(max_length=128, blank=True)
    activation_key_expiring = models.DateTimeField(default=(now() + timedelta(hours=48)))

    def activation_key_expired(self):
        return now() >= self.activation_key_expiring


class UserProfile(models.Model):
    MALE = 'M'
    FEMALE = 'W'

    GENDER_CHOICE = (
        (MALE, 'М'),
        (FEMALE, 'Ж'),
    )

    user = models.OneToOneField(User, null=False, db_index=True, unique=True, on_delete=models.CASCADE)

    tagline = models.CharField(verbose_name='тэги', max_length=128, blank=True)
    about_me = models.TextField(verbose_name='обо мне', max_length=512, blank=True)
    gender = models.CharField(verbose_name='пол', choices=GENDER_CHOICE, max_length=1, blank=True)

    @receiver(signal=post_save, sender=User)
    def create_profile(sender, instance, created, **kwargs):
        if created:
            UserProfile.objects.create(user=instance)

    @receiver(signal=post_save, sender=User)
    def update_profile(sender, instance, **kwargs):
        instance.userprofile.save()
