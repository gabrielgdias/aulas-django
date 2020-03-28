from django.db.models.signals import post_save, post_delete
from django.dispatch import  receiver
from django.contrib.auth.models import User
from .models import UserProfile

@receiver(post_save, sender=User)
def creta_user_profile(sender, instance, created, **kwargs):
    user = instance
    if created:
        UserProfile.objects.create(user=user)

@receiver(post_delete, sender=User)
def send_email(sender, instance, **kwargs):
    user = instance
    print("muito obrigado "+ user.username +" por ter participado da plataforma")