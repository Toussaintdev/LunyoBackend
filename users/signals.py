from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import User, Profil

@receiver(post_save, sender=User)
def create_user_profil(sender, instance, created, **kwargs):
    if(created):
        Profil.objects.create(user=instance)




