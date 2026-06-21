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
    status = models.CharField(max_length=20 ,choices=UserStatus.choices, default=UserStatus.ACTIVE)
    email = models.EmailField(unique=True, blank=False, null=False)

    class Meta:
        ordering = ['-date_joined']

    def __str__(self):
        return self.username
    
def upload_profil_image(instance, filename):
    ext = filename.split('.')[-1]
    newname = f'profil_lunyo_{instance.user.id}.{ext}'
    return f'lunyo/profil/{newname}'

class Profil(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    bio = models.CharField(max_length=200, blank=True)
    photo = models.ImageField(upload_to=upload_profil_image, blank=True, null=True)
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profil")

    class Meta:
        ordering=["-createdAt"]

    def __str__(self):
        return f'Profil de {self.user.username}'
