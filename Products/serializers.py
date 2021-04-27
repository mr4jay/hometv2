from rest_framework import serializers
from .models import FoodProducts


class ProductSerializer(serializers.ModelSerializer):
    
      class Meta:
         model = FoodProducts
         fields = "__all__"
      

# class LoginSerializer(serializers.Serializer):
#       email = serializers.CharField()
#       password = serializers.CharField()


# class ChangePasswordSerializer(serializers.Serializer):
#       old_password = serializers.CharField()
#       new_password = serializers.CharField()


# class ResetPasswordLinkSerializer(serializers.Serializer):
#       email= serializers.EmailField()


# class ResetPasswordsSerializer(serializers.Serializer):
#       password = serializers.CharField()
#       confirm_password = serializers.CharField()

     