
from django.urls import path,include
from .views import *
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    path('create_user/',csrf_exempt(CreateUser.as_view())),
    path('Login_user/',csrf_exempt(Login.as_view())),
    path('Logout_user/',logout_view.as_view()),
    path('changepassword/',changepassword.as_view()),
    path('resetpasswordlink/',ResetPasswordLink.as_view()),
    path('resetpassword/<str:email_time>',ResetPassword.as_view())

]
