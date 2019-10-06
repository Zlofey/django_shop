from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.db import models


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # first_name = models.CharField(verbose_name='Имя', max_length=50, blank=True)
    # last_name = models.CharField(verbose_name='Фамилия', max_length=50, blank=True)
    # email = models.EmailField(verbose_name='Email', blank=True)
    address = models.CharField(verbose_name='Адрес', max_length=250, blank=True)
    postal_code = models.CharField(verbose_name='Почтовый индекс', max_length=20, blank=True)
    city = models.CharField(verbose_name='Город', max_length=100, blank=True)

@receiver(post_save, sender=User)
def new_user(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()