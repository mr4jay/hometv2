from rest_framework import serializers
from .models import *


class CustomerOrdersSerializer(serializers.ModelSerializer):
    
      class Meta:
         model = CustomerOrders
         fields = "__all__"
         write_only = 'customers'
         
class CustomerCartSerializer(serializers.ModelSerializer):
    
      class Meta:
         model = CutomerCart
         fields = "__all__"
        
        

# class LoginSerializer(serializers.Serializer):
#       email = serializers.CharField()
#       password = serializers.CharField()



     