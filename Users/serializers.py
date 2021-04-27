from rest_framework import serializers
from .models import User


class UserSerializer(serializers.ModelSerializer):
      password2 = serializers.CharField(max_length= 50)
      class Meta:
         model = User
         fields = ('email', 'name','phone', 'password','password2')

      def create(self, validated_data):
        user = User( email=validated_data['email'], name=validated_data['name'], phone = validated_data['phone'])
        user.set_password(validated_data['password'])
        user.save()
        return user

class LoginSerializer(serializers.Serializer):
      email = serializers.CharField()
      password = serializers.CharField()


class ChangePasswordSerializer(serializers.Serializer):
      old_password = serializers.CharField()
      new_password = serializers.CharField()


class ResetPasswordLinkSerializer(serializers.Serializer):
      email= serializers.EmailField()


class ResetPasswordsSerializer(serializers.Serializer):
      password = serializers.CharField()
      confirm_password = serializers.CharField()

     