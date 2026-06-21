from rest_framework import serializers
from .models import User, Profil

class UserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(required=True)
    password = serializers.CharField(write_only=True, min_length=4)
    password2 = serializers.CharField(write_only=True)
    
    class Meta:
        model = User
        fields = ["id", "username", "password", "password2", "email", "status"]
        read_only_fields = ["id", "status"]

    def validate_email(self, value):
        if User.objects.filter(email=value).exists():
            raise serializers.ValidationError("Email invalide")
        return value

    def validate(self, data):
        if data['password'] != data['password2']:
            raise serializers.ValidationError(
                {'password': "Les mots de passe ne correspondent pas"}
            )
        return data

    def create(self, validated_data):
        validated_data.pop('password2')
        user = User.objects.create_user(**validated_data)
        return user


class ProfilSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profil
        fields=['id','bio', 'photo', 'user']
        read_only_fields = ['id', 'user']
        