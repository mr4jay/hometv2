
from django.urls import path,include
from .views import *


urlpatterns = [
    path('create_order/',CreateOrders.as_view()),
    # path('update_order/<int:pk>',UpdateOrders.as_view()),
    path('add_to_cart/',CustomerCart.as_view()),
    
]
