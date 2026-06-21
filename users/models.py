from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid

# la classe ennumeration pour definir statu de l'utilisateur
class UserStatus(models.TextChoices):
    """Statu de l'utilisateur"""
    ACTIVE = 'active', 'Actif'
    INACTIVE = 'inactive', 'Inactif'
    DELETED = 'deleted', 'Supprimé'
    BANNED = 'banned', 'Banni'

class User(AbstractUser):
    """La classe User personnalisée"""
    id = models.UUIDField(primary_key = True, default = uuid.uuid4, editable = False)
    status = models.CharField(max_length=20 ,choices=UserStatus, default=UserStatus.ACTIVE)

    class Meta:
        ordering = ['-date_joined']

    def __str__(self):
        return self.username
    
class Profil(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    bio = models.CharField(max_length=200, blank=True, null=True)
    photo = models.ImageField(upload_to="lunyo/profil/")
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profil")