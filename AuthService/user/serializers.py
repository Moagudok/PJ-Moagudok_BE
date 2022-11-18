from rest_framework import serializers
from sharedb.models import User as UserModel

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserModel
        fields = "__all__"
    
    def create(self, *args, **kwargs):
        user = super().create(*args, **kwargs)
        password = user.password
        user.set_password(password)
        user.save()
        return user

    def update(self, *args, **kwargs):
        user = super().update(*args, **kwargs)
        password = user.password
        user.set_password(password)
        user.save()
        return user
        

class LoginUserSerializer(serializers.Serializer):
    email = serializers.EmailField()
    is_seller = serializers.BooleanField()
    password = serializers.CharField(write_only=True)