from django.shortcuts import render

# Create your views here.
from   django.shortcuts        import   render
from   rest_framework.views    import   APIView
from   rest_framework          import   status
from   .models                 import   *
from   rest_framework          import   generics
from   .serializers            import   *
from   rest_framework.response import   Response
from   django.core.mail        import   send_mail
from   datetime                import   datetime



class CustomerCart(generics.CreateAPIView):
    serializer_class = CustomerCartSerializer

    def get(self,request,format= None):

        try:
            queryset = CutomerCart.objects.filter(customer_details =request.user).all().values()
            return Response(queryset)
        except:
            return Response("Add to cart")

    def post(self,request,format = None):
        serializer = CustomerCartSerializer(data = request.data)
        if serializer.is_valid():
             serializer.validated_data['customer_details'] = self.request.user
             try:
                CutomerCart.objects.filter(customer_details =request.user).delete()
             except:
                pass
             serializer.save()
             return Response({"message": "added to cart"})
        return Response({'message': list(serializer.errors.keys())[0]+' - '+list(serializer.errors.values())[0][0]}, status=status.HTTP_200_OK)







class CreateOrders(generics.CreateAPIView):
    
    serializer_class = CustomerOrdersSerializer
    def get(self,request,format = None):
        

        data={}
        #customer data
        data['customer']  = request.user
        data['name']      = request.user.name
        data['mail']      = request.user.email
        data['location']  = request.user.address1

        #order data
        try:
            order_data = CutomerCart.objects.filter(customer_details= request.user).all().values()
            orders = order_data[0]['orders']
            data['orders'] =[]
            data['order_price']=0

            for i in orders:
                data['orders'].append({'item_name': i['item_name'],'item_price': i['item_price']})
                data['order_price']=data['order_price'] + i['item_price']

        except:
            return Response("your cart is empty")
        
        

        # data['ordered_date_time']=datetime.now()
        data['ordered_quantity'] =len(orders)
        data['delivery_charges']=30
        data['discount']=0
        data['final_price']= data['order_price']+data['delivery_charges']-int((data['order_price']*data['discount'])/100)

        #payment data
        data['mode_of_payment']="Online"
        data['is_paid']=0

        #delivery data
        data['delivery_person_name']="Somexyz"
        data['delivery_person_phone']="9999"
        data['is_delivered']=0
        data['is_canceled']=0
        data['reason_for_cancel']=0

        serializer = CustomerOrdersSerializer(data)
   
    

        return Response(serializer.data)

        # return Response({'message': list(serializer.errors.keys())[0]+' - '+list(serializer.errors.values())[0][0]}, status=status.HTTP_200_OK)


    def post(self, request, format=None):
        serializer = CustomerOrdersSerializer(data=request.data)
        if serializer.is_valid():
            serializer.validated_data['customer'] = self.request.user
            customer = serializer.validated_data['customer']
            serializer.validated_data['ordered_date_time']=datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            print(customer.name)
            serializer.save()
            CutomerCart.objects.filter(customer_details =request.user).delete()
            return Response({"message": serializer.data }, status=status.HTTP_201_CREATED)
            
        return Response({'message': list(serializer.errors.keys())[0]+' - '+list(serializer.errors.values())[0][0]}, status=status.HTTP_200_OK)














































# class UpdateOrders(APIView):
#     serializer_class =CustomerOrdersSerializer

#     def get(self,request,pk):
#         queryset = CustomerOrders.objects.all().filter(pk = pk).values()
#         return Response(queryset)

#     def patch(self, request,pk):
#         update_object = CustomerOrders.objects.get(pk= pk)
#         serializer = CustomerOrdersSerializer(update_object, data=request.data, partial=True)
#         if serializer.is_valid():
#             serializer.save()
#             return Response( data=serializer.data)
#         return Response( data="wrong parameters")
