from rest_framework import serializers
from sharedb.models import User

class UserSignUpSerializers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
        
    def create(self, *args, **kwargs):
        user = super().create(*args, **kwargs)
        p = user.password
        user.set_password(p)
        user.save()
        return user
    
    def update(self, *args, **kwargs):
        user = super().update(*args, **kwargs)
        p = user.password
        user.set_password(p)
        user.save()
        return user