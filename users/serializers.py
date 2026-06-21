from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, min_length=4)
    password2 = serializers.CharField(write_only=True)
    
    class Meta:
        model = User
        fields = ["id", "username", "password", "password2", "email", "status"]
        read_only_fields = ["id", "status"]

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
    # pour le statu, c'est un admin qui peut faire certains choses, l'utilisateur aussi d'autres

