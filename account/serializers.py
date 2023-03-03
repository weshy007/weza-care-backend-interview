from djoser.serializers import UserSerializer as BaseUserSerializer, UserCreateSerializer as BaseUserCreateSerializer

from .models import CustomUser


class UserSerializers(BaseUserSerializer):
    class Meta(BaseUserSerializer.Meta):
        model = CustomUser
        fields = ['username', 'first_name', 'last_name', 'email']


class UserCreateSerializer(BaseUserSerializer):
    class Meta(BaseUserCreateSerializer.Meta):
        model = CustomUser
        fields = ['username', 'first_name', 'last_name', 'email', 'password']
