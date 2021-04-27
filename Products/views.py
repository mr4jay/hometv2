from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import status
from .models import FoodProducts
from rest_framework import generics
from .serializers import *
from rest_framework.response import Response

from django.core.mail import send_mail
from datetime import datetime


class CreateProducts(generics.CreateAPIView):
    
    serializer_class = ProductSerializer

    def get(self,request,format=None):
        queryset = FoodProducts.objects.all().values()
        return Response (queryset)

    def post(self, request, format=None):
        serializer = ProductSerializer(data=request.data,many = True)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Success"}, status=status.HTTP_201_CREATED)
            
        return Response({'message': list(serializer.errors.keys())[0]+' - '+list(serializer.errors.values())[0][0]}, status=status.HTTP_200_OK)

class UpdateProducts(APIView):
    serializer_class =ProductSerializer

    def get(self,request,pk):
        queryset = FoodProducts.objects.all().filter(pk = pk).values()
        return Response(queryset)

    def patch(self, request,pk):
        update_object = FoodProducts.objects.get(pk= pk)
        serializer = ProductSerializer(update_object, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response( data=serializer.data)
        return Response( data="wrong parameters")


class get_items(APIView):
    serializer_class = ProductSerializer
    def get(self,request,format = None):
        queryset = FoodProducts.objects.all()
        
        if request.query_params['item_name']:
            queryset = queryset.filter(item_name__icontains = request.query_params['item_name'])

        # if request.query_params['item_type']:
        #     queryset = queryset.filter(item_type__icontains = request.query_params['item_type'])
            
        if request.query_params['made_of_category']:
            queryset = queryset.filter(made_of_category__icontains = request.query_params['made_of_category'])
            
        if request.query_params['material_used']:
            queryset = queryset.filter(material_used__icontains = request.query_params['material_used'])
            
        if request.query_params['item_price']:
            queryset = queryset.filter(item_price__lte = request.query_params['item_price'])
            

        
        return Response({"data":queryset.values()})

