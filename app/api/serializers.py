from app.models import UserRegisterModel
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserRegisterModel
        fields = '__all__'