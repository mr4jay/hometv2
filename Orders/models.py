from django.db       import models
from Users.models    import *
from Products.models import *
from django.core.validators import RegexValidator

# Create your models here.
class CustomerOrders(models.Model):
    int_validator     = RegexValidator(regex=r'^[0-9]')

    #Customer Related Fileds
    customer          = models.ForeignKey(User, on_delete=models.CASCADE,null=True,blank=True ,default= None)
    name              = models.CharField(max_length=50,null=True,blank=True ,default= None)
    mail              = models.EmailField(max_length=50,null=True,blank=True ,default= None)
    phone             = models.CharField(max_length= 10,null=True,blank=True,validators=[int_validator])
    location          = models.TextField(null=True,blank=True)

    #Order Related Fields
    orders            = models.TextField(default = None)
    ordered_date_time = models.DateTimeField(auto_now_add=False,null=True,blank=True)
    ordered_quantity  = models.CharField(max_length = 3, null= True, blank= True,validators=[int_validator])
    order_price       = models.CharField(max_length = 3, null=True,blank=True, validators=[int_validator])
    delivery_charges  = models.CharField(max_length = 3, null=True,blank=True, validators=[int_validator])
    discount          = models.CharField(max_length = 3, null=True,blank=True,validators=[int_validator],verbose_name="coupon")
    final_price       = models.CharField(max_length = 3, null=True,blank=True,validators=[int_validator])

    #payment related fields
    mode_of_payment = models.CharField(max_length=20,null=True,blank=True ,default= None)
    is_paid         = models.BooleanField(default=False) 

    #Delivery Related Fileds
    delivery_person_name   = models.CharField(max_length=30,null=True,blank=True)
    delivery_person_phone  = models.CharField(max_length = 10, null=True,blank=True, validators=[int_validator])
    is_delivered           = models.BooleanField(null=True,blank=True ,default = False)
    is_canceled            = models.BooleanField(null=True,blank=True ,default = False)
    reason_for_cancel      = models.TextField(null=True, blank=True)

class CutomerCart(models.Model):
    customer_details = models.ForeignKey(User,on_delete= models.CASCADE,null=True,blank=True,default=None)
    orders = models.JSONField()



