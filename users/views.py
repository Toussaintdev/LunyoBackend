from django.shortcuts import get_object_or_404
from rest_framework import generics
from .serializers import UserSerializer, ProfilSerializer
from .models import User, Profil, UserStatus
from rest_framework import permissions
from .permissions import IsSelf, IsSelfOrAdmin

# view d'inscription
class InscriptionView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]
    authentication_classes = []

# view de la liste de tous les utilisateurs 
class UserListView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes=[permissions.AllowAny]
    authentication_classes = []

# view du detail de chaque utiisateur et la modification sécurisée
class UserDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes=[IsSelfOrAdmin]

    def perform_destroy(self, instance):
        instance.status = UserStatus.DELETED
        instance.save()

# view de retour du profil de l'utilisateur connecté et la mise a jour du profil
class ProfilCurrentView(generics.RetrieveUpdateAPIView):
    serializer_class = ProfilSerializer
    permission_classes = [permissions.IsAuthenticated ,IsSelf]
    def get_object(self):
        user = self.request.user
        return get_object_or_404(Profil, user=user)
    
# view de profil de chaque utilisateur
class ProfilView(generics.RetrieveAPIView):
    serializer_class=ProfilSerializer
    permission_classes=[permissions.AllowAny]
    def get_object(self):
        username = self.kwargs['username']
        user = get_object_or_404(User, username=username)
        return get_object_or_404(Profil, user=user)


# class ProfilCreateView(generics.CreateAPIView):
#     queryset = Profil.objects.all()
#     serializer_class = ProfilSerializer

#     def perform_create(self, serializer):
#         serializer.save(user=self.request.user)
#     # la classe va etre appelé juste en cas de non fonctionnement du signal de creation de profil apres inscription