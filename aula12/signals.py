from django.db.models.signals import pre_save
from django.dispatch import  receiver
from django.contrib.auth.models import User
from .models import Automovel
from slugify import slugify


@receiver(pre_save, sender=Automovel)
def creta_user_profile(sender, instance, **kwargs):
    automovel = instance
    automovel.slug = slugify(automovel.marca + " " + automovel.modelo)
    