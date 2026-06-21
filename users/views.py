from django.shortcuts import get_object_or_404
from rest_framework import generics
from .serializers import UserSerializer, ProfilSerializer
from .models import User, Profil, UserStatus
from rest_framework import permissions
from .permissions import IsSelf, IsSelfOrAdmin

class InscriptionView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]

class UserListView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes=[permissions.AllowAny]

class UserDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes=[IsSelfOrAdmin]

    def perform_destroy(self, instance):
        instance.status = UserStatus.DELETED
        instance.save()

class ProfilCurrentView(generics.RetrieveUpdateAPIView):
    serializer_class = ProfilSerializer
    permission_classes = [permissions.IsAuthenticated ,IsSelf]
    def get_object(self):
        user = self.request.user
        return get_object_or_404(Profil, user=user)
    
    
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