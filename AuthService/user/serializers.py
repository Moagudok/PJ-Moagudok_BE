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
    
    def validate_name(self, data):
        if len(data) < 2:
            raise serializers.ValidationError("이름은 2자 이상이어야 합니다.")
        return data
    def validate_password(self, data):
        if not data:
            raise serializers.ValidationError("비밀번호를 입력해주세요")
        if len(data) < 8:
            raise serializers.ValidationError("비밀번호는 8자 이상이어야 합니다.")
        return data
    def validate_address(self, data):
        if len(data) < 5:
            raise serializers.ValidationError("주소는 5자 이상이어야 합니다.")
        return data

class LoginUserSerializer(serializers.Serializer):
    email = serializers.EmailField()
    is_seller = serializers.BooleanField()
    password = serializers.CharField(write_only=True)