from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import status
from .models import User
from rest_framework import generics
from .serializers import *
from rest_framework.response import Response
from django.contrib.auth import authenticate, login, logout
from django.core.mail import send_mail
from datetime import datetime
from cryptography.fernet import Fernet

key = Fernet.generate_key()
fernet = Fernet(key)
# Create your views here.
class CreateUser(generics.CreateAPIView):

    serializer_class = UserSerializer
    def post(self, request, format=None):

        serializer = UserSerializer(data=request.data)

        if serializer.is_valid():
            if serializer.validated_data['password'] == serializer.validated_data['password2']:
                serializer.save()

            # # Sending Mail of Credentials
            #     data = "username:  " + str(serializer.validated_data['email']) + "\n password:  "+ str(serializer.validated_data['password'])
            #     send_mail("Home Food Kitchens : Login Credentials ",
            #               data,
            #               "bhavanigloled@gmail.com",
            #               [serializer.validated_data['email']])
            # # Sending Mail Ends
                
                return Response({"message": "Success"}, status=status.HTTP_201_CREATED)
            else:
                return Response("Password did'nt match")
        return Response({'message': list(serializer.errors.keys())[0]+' - '+list(serializer.errors.values())[0][0]}, status=status.HTTP_200_OK)


class Login (generics.CreateAPIView):
   serializer_class = LoginSerializer

   def post(self, request, fromat=None):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            try:
                user = authenticate(email=serializer.validated_data['email'], password=serializer.validated_data['password'])
                print(user)
            except:
                return Response({"message": 'Invalid Credentials'},status=status.HTTP_200_OK)

            if user is not None:
                if user.is_active :
                    login(request, user)

            # # Sending Mail of Login Activity
            #     ip = self.request.META.get('HTTP_X_FORWARDED_FOR', self.request.META.get('REMOTE_ADDR', '')).split(',')[0].strip()
            #     date = "Login Time:  " + str(datetime.now().strftime("%B %d %Y %H:%M:%S"))
            #     data = "We Found a New Login ip_address:  "+ str(ip) +"\n"+ date
                
            #     send_mail("Login Alert",
            #               data,
            #               "bhavanigloled@gmail.com",
            #               [serializer.validated_data['email']])
            # # Sending Mail Ends
                
                return Response({"User Authenticated":request.user.is_authenticated, "message":"Login Sucessful"})
            else:
                return Response({"message": 'Invalid Credentials'},status=status.HTTP_200_OK)

        return Response({'message': list(serializer.errors.keys())[0]+' - '+list(serializer.errors.values())[0][0]}, status=status.HTTP_200_OK)


class logout_view(APIView):
    
     def get(self, request, fromat=None):
         logout(request)
         return Response("Logout Sucessfull")


class changepassword(APIView):

    serializer_class = ChangePasswordSerializer
    def post(self,request,format = None):
        try:
            user = request.user
        except:
            Response("Login First")

        serializer=  ChangePasswordSerializer(data = request.data)
        if serializer.is_valid():

            if user.check_password(serializer.data['old_password']):
                new_password = serializer.data['new_password']
                user.set_password(serializer.data['new_password'])
                request.user.save()

            # Sending Mail of Login Activity
                ip = self.request.META.get('HTTP_X_FORWARDED_FOR', self.request.META.get('REMOTE_ADDR', '')).split(',')[0].strip()
                data = "ip address :  "+ str(ip)+ "\n"
                message =" Your Password was updated \n "
                date = "Updated Time:  " + str(datetime.now().strftime("%B %d %Y %H:%M:%S"))
                data = message + data + "new password:  "+str(new_password) + '\n' + date
                send_mail("Password Changed", data, "bhavanigloled@gmail.com", [user.email])
            # Sending Mail Ends
           
                return Response("Password Changed")
            else:
                return Response("Pasword didnt match")


class ResetPasswordLink(APIView):
    serializer_class = ResetPasswordLinkSerializer

    def post(self,request,format = None):
        serializer = ResetPasswordLinkSerializer(data = request.data)

        if serializer.is_valid():
            time = str(datetime.now())

            try:
                user = User.objects.get(email = serializer.data['email'])

                email_time = serializer.data['email']+'\n'+time
                email_time = fernet.encrypt(email_time.encode())
                email_time = str(email_time)[2:-1]

                data = "http://127.0.0.1:8000/apis/Users/resetpassword/"+email_time

                send_mail("Reset Password request", data, "bhavanigloled@gmail.com", [serializer.data['email']])

                return Response("reset link successfully sent to your registered mail id")

            except:
                return Response("Enter a valid email address.")

        return Response("Enter a valid email address.")


class ResetPassword(APIView):
    serializer_class = ResetPasswordsSerializer
    def post(self,request,email_time,format = None):
        endtime= datetime.now()
        serializer = ResetPasswordsSerializer(data = request.data)

        email_time= bytes(email_time,'utf-8')
        email_time = fernet.decrypt(email_time).decode()
        email_time = email_time.split('\n')


        try:
            user = User.objects.get(email = email_time[0])
        except:
            return Response("Invalid Email Id")
    
        if serializer.is_valid():
            
            starttime=datetime.strptime(email_time[1],'%Y-%m-%d %H:%M:%S.%f')
            diff = endtime-starttime
            if diff.seconds >60 :
                return Response("Request Time Out ")
            
            if serializer.data['password']!=serializer.data['confirm_password']:
                return Response("Both Passwords must be same")

            user.set_password(serializer.data['password'])
            user.save()
            send_mail("Password Reset  Sucessful "," You're password has been successfully changed", "bhavanigloled@gmail.com", [email_time[0]])
            
            return Response ("password reset sucessful")
        else:
            return Response("ok")


