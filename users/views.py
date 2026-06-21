from django.shortcuts import render
from rest_framework import generics, mixins
from .serializers import UserSerializer
from .models import User

# utilisation de generics create
class InscriptionView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer