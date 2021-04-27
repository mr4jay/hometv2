
from django.urls import path,include
from .views import *


urlpatterns = [

    path('add_new_product/',CreateProducts.as_view()),
    path('update_product/<int:pk>',UpdateProducts.as_view()),
    path('get_items/',get_items.as_view()),

    
    
]
